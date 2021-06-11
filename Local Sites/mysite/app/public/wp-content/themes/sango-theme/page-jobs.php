<?php get_header(); ?>
<?php if(is_front_page()) get_template_part('parts/home/featured-header'); ?>
  <div id="content">
    <div id="inner-content__jobs" class="wrap cf">
      <div class="page-logo__jobs">
        <a href="<?php echo esc_url( home_url( '/category/frontend-engineer' ) ); ?>"><img src="<?php echo get_template_directory_uri(); ?>/library/images/frontend-engineer.png"></a>
      </div>
      <div class="page-logo__jobs">
        <a href="<?php echo esc_url( home_url( '/category/backend-engineer' ) ); ?>"><img src="<?php echo get_template_directory_uri(); ?>/library/images/backend-engineer.png"></a>
      </div>
      <div class="page-logo__jobs">
        <a href="<?php echo esc_url( home_url( '/category/web-marketer' ) ); ?>"><img src="<?php echo get_template_directory_uri(); ?>/library/images/web-marketer.png"></a>
      </div>
      <main id="main" class="m-all t-2of3 d-5of7 cf">
        
      </main>
      <?php get_sidebar(); ?>
    </div>
  </div>
<?php get_footer(); ?>
