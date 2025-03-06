
himanthad4@gmail.com
0768840107
Himantha123&@




admin

himantha123
hima




now you know header and footer acutal things,. now we going to redesign enetire home page


{% extends "base.html" %}
{% block title %}Home - MephubLK{% endblock %}
{% block content %}
<!-- Hero Section -->
{% load static %}
<div class="jumbotron text-center text-white" style="background: url('{% static 'images/hero.webp' %}') no-repeat center center; background-size: cover; position: relative; height: 400px;">
  <div style="background-color: rgba(0,0,0,0.5); position: absolute; width: 100%; height: 100%; top: 0; left: 0;"></div>
  <div class="container" style="position: relative; z-index: 2;">
    <h1 class="display-4">Connecting Sri Lanka’s Construction Experts with You</h1>
    <form action="" method="get" class="mt-4">
      <div class="input-group input-group-lg">
        <input type="text" name="q" class="form-control" placeholder="Search for Consultants, Contractors, etc.">
        <button type="submit" class="btn btn-outline-light">Search</button>
      </div>
    </form>
    <div class="mt-4">
      <a href="" class="btn btn-primary btn-lg mr-2">Browse Categories</a>
      <a href="" class="btn btn-success btn-lg">Register as an Expert</a>
    </div>
  </div>
</div>

<!-- Categories Section -->
<div class="my-5">
  <h2 class="text-center">Categories</h2>
  <div class="row">
    {% for category in categories %}
      <div class="col-md-3 text-center">
        <div class="card">
          <div class="card-body">
            <img src="{{ category.icon.url }}" alt="{{ category.name }}" style="width:60px;">
            <h5 class="card-title mt-2">{{ category.name }}</h5>
            <p class="card-text">{{ category.description }}</p>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Featured Profiles Section -->
<div class="my-5">
  <h2 class="text-center">Featured Profiles</h2>
  <div class="row">
    {% for profile in featured_profiles %}
      <div class="col-md-4">
        <div class="card">
          <img src="{{ profile.image.url }}" class="card-img-top" alt="{{ profile.name }}">
          <div class="card-body">
            <h5 class="card-title">{{ profile.name }}</h5>
            <p class="card-text">{{ profile.profession }}</p>
            <a href="{% url 'profiles:profile_detail' profile.id %}" class="btn btn-primary">View Profile</a>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Testimonials Section -->
<div class="my-5">
  <h2 class="text-center">What Our Users Say</h2>
  <div class="row">
    {% for testimonial in testimonials %}
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <p class="card-text">"{{ testimonial.content }}"</p>
            <footer class="blockquote-footer">{{ testimonial.author }}</footer>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<!-- Call-to-Action Banner -->
<div class="jumbotron text-center" style="background-color: #E67E22;">
  <h2 class="display-4 text-white">Join MephubLK Today!</h2>
  <p class="lead text-white">Connect with top construction experts across Sri Lanka.</p>
  <a href="" class="btn btn-light btn-lg">Register Now</a>
</div>
{% endblock %}


this is exist home page. but this is not even give the idea. clearly correctly undertand this website type. this is hiome page that users land and seeking for there profesionals, see upcoming prject sileds, limportant things, experts profile view section(when user regiter in systems ans each experts or lerning platform or servide or any those are nicely show in nice places niely screen resposniec and in clean proesional industrial way. develiop actal home page with dummy data that represent lankan stre,clean and modrn screen resposive look is muts. provide you best code )


you must design whole page again that matcghin with header nad footer andwen sidea. dont iuse two much blkue or dont use tellow. use blue lines only if need. use clean ui.