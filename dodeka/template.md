# Twelve-Factor App Checklist
{%- block list %}
{% for factor in factors %}
  - [ ] {{ factor.title }}: {{ factor.short_description }}
{% endfor %}
{% endblock -%}