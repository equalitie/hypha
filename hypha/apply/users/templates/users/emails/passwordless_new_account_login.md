{% load i18n wagtailadmin_tags %}{% base_url_setting as base_url %}
{% blocktrans %}Hello {% endblocktrans %}

{% blocktrans %}Thank you for registering an account on eQualitie's *Grant Programs & Opportunities* application system. Finish account creation by clicking the link below or copy/paste it in your browser:
{% endblocktrans %}

{% if site %}{{ site.root_url }}{% else %}{{ base_url }}{% endif %}{{ signup_path }}

{% blocktrans %}This link will be valid for {{ timeout_minutes }} minutes and can be used only once.{% endblocktrans %}

{% blocktrans %}If you did not request this email, please ignore it.{% endblocktrans %}

{% if org_email %}
{% blocktrans %}If you have any questions, please contact us at {{ org_email }}.{% endblocktrans %}
{% endif %}

{% blocktrans %}Regards,{% endblocktrans %}

--
{{ org_long_name }}
https://equalit.ie
