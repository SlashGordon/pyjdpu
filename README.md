# pyjdpu

[![Build Status](https://travis-ci.org/SlashGordon/pyjdpu.svg?branch=master)](https://travis-ci.org/SlashGordon/pyjdpu)
[![Coverage Status](https://coveralls.io/repos/github/SlashGordon/pyjdpu/badge.svg?branch=master)](https://coveralls.io/github/SlashGordon/pyjdpu?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26e80c8a34e74a7395bd41409b2b9f75)](https://www.codacy.com/manual/SlashGordon/pyjdpu?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SlashGordon/pyjdpu&amp;utm_campaign=Badge_Grade)

Sometimes you have to update many plugins during jenkins docker upgrade and waste a lot of time.
With  pyjdpu you can easily update your plugins.txt automaticly to the latest versions.


## install

```shell
pip install pyjdpu
```

## quick start
Update your plugins.txt wit cli:

```bash
pyjdpu -i plugins.txt -o plugins_updated.txt

```

Get latest version of an jenkins plugin:

```python
import pyjdpu
my_api = pyjdpu.JenkinsPluginApi()
my_version = my_api.get_latest_version('blueocean-git-pipeline')

```

## issue tracker

[https://github.com/portfolioplus/pystockfilter/issuese](https://github.com/SlashGordon/pyjdpu/issues")
