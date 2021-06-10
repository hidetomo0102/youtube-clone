<?php get_header(); ?>
<?php if(is_front_page()) get_template_part('parts/home/featured-header'); ?>
  <div id="content">
    <div id="inner-content" class="wrap cf">
      <main id="main" class="m-all t-2of3 d-5of7 cf">
        
      </main>
      <?php get_sidebar(); ?>
    </div>
  </div>
<?php get_footer(); ?>
