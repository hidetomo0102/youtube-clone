<?php get_header(); ?>
  <div id="content">
    <div id="inner-content__popular" class="wrap cf popular">
      <div class="tagcloud">
        <?php wp_tag_cloud(); ?>
      </div>
      <div class="page-logo">
        <a href="<?php echo esc_url( home_url( '/popular' ) ); ?>"><img src="<?php echo get_template_directory_uri(); ?>/library/images/popular.png"></a>
      </div>
      <main id="main" class="m-all t-2of3 d-5of7 cf">
        <div class="cardtype cf">
        <article class="cardtype__article">
            <a class="cardtype__link" href="http://mysite.local/9%e3%81%a4%e7%9b%ae%e3%81%ae%e8%a8%98%e4%ba%8b%e3%81%a7%e3%81%99%e3%80%82/">
              <p class="cardtype__img">
                <img src="http://mysite.local/wp-content/themes/sango-theme/library/images/default_small.jpg" alt="9つ目の記事です。">
              </p>
              <div class="cardtype__article-info">
                <time class="pubdate entry-time dfont" itemprop="datePublished" datetime="2021-06-11">
                  2021-06-11
                </time>
                <h2>9つ目の記事です。</h2>
              </div>
            </a>
            <a href="http://mysite.local/category/backend-engineer/" class="dfont cat-name catid9">バックエンドエンジニア</a>
          </article>
        </div>
      </main>
      <?php get_sidebar(); ?>
    </div>
  </div>
<?php get_footer(); ?>