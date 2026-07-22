(fw-governance-roles)=
# Roles

## Steering Committee

:::{substitution}
| role | person |
| --- | --- |
{% for key, role in roles %} {% if role.level == "constitutional" %} | {{ role.name }} | {% set comma = joiner() %} {% for person in role.incumbent -%} {{ comma() }} [](#profile-{{ person.id }}) {%- endfor %} |
{% endif %} {% endfor %}
:::
