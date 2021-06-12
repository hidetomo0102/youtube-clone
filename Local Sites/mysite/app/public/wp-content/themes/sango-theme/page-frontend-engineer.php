<?php get_header(); ?>
  <div id="content">
    <div id="inner-content__popular" class="wrap cf popular">
      <div class="tagcloud">
        <?php wp_tag_cloud(); ?>
      </div>
      <div class="page-logo">
        <a href="<?php echo esc_url( home_url( '/frontend-engineer' ) ); ?>"><img src="<?php echo get_template_directory_uri(); ?>/library/images/frontend-engineer.png"></a>
      </div>
      <main id="main" class="m-all t-2of3 d-5of7 cf">
        <div class="cardtype cf">
          <?php
            $cat_id = get_cat_ID( 'フロントエンドエンジニア' );
            if ( $cat_id ) {
              $args = array(
                'posts_per_page' => 9, // 表示件数の指定
                'category' => $cat_id,
              );
              $posts = get_posts( $args );
              foreach ( $posts as $post ): // ループの開始
              setup_postdata( $post ); // 記事データの取得
              $id = $post->ID;
          ?>
            <article class="cardtype__article">
              <a class="cardtype__link" href="<?php the_permalink(); ?>">
              <p class="cardtype__img">
                <img src="<?php echo featured_image_src('thumb-520'); ?>" alt="<?php the_title(); ?>" width="520" height="300">
              </p>
              <div class="cardtype__article-info">
                <time class="pubdate entry-time dfont" itemprop="datePublished" datetime="<?php echo get_the_date('Y-m-d', $id) ?>">
                  <?php echo get_the_date('Y-m-d', $id) ?>
                </time>
                <h2><?php the_title(); ?></h2>
              </div>
            </a>
            </article>
          <?php
            endforeach;
            wp_reset_postdata(); // 直前のクエリを復元する
          }
          ?>
        </div>
      </main>
      <?php get_sidebar(); ?>
    </div>
  </div>
<?php get_footer(); ?>