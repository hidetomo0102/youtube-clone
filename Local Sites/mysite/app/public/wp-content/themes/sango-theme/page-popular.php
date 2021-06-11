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
        
      </main>
      <?php get_sidebar(); ?>
    </div>
  </div>
<?php get_footer(); ?>