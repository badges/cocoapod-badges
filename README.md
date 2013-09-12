Cocoapod Badges [![Build Status](https://travis-ci.org/fjcaetano/cocoapod-badges.png)](https://travis-ci.org/fjcaetano/cocoapod-badges)
===============

[![Badge w/ Version](http://cocoapod-badges.herokuapp.com/v/NSStringMask/badge.png)](http://cocoadocs.org/docsets/NSStringMask)
[![Badge w/ Platform](http://cocoapod-badges.herokuapp.com/p/NSStringMask/badge.svg)](http://cocoadocs.org/docsets/NSStringMask)

Cocoapod Badges are status badges to inform a pod's latest version deployed to [Cocoapods] through their [simple API](https://github.com/CocoaPods/cocoapods.org/commit/8ef51c7890c33ad899e8130b9e778c740c5c7f61).

The badges are created with a `SVG` file, thanks to [olivierlacan/shields](https://github.com/olivierlacan/shields) repo that provides badges to:

- [Code Climate](https://codeclimate.com/changelog/510d4fde56b102523a0004bf)
- [Coveralls](https://coveralls.io/r/kaize/nastachku)
- [Gemfury/RubyGems](http://badge.fury.io/)
- [Gemnasium](http://blog.tech-angels.com/post/43141047457/gemnasium-v3-aka-gemnasium)
- [Travis CI](http://about.travis-ci.org/docs/user/status-images/)

The "badge service" is hosted at [Heroku](https://www.heroku.com/)

# Usage

Just replace the `$PODNAME` on the URLs and the badge will automatically fetch the info.

**_ATTENTION_**: The `$PODNAME` is case sensitive, since [Cocoapods] has differentiation! In case of unexpected issues, the badges will display "error".

The badges might be displayed as SVG or PNG, depending on the requested extension, though we strongly recommend using SVG since it's rendering is much better than PNG. But be aware that it may cause some problems with some browsers.

## Retina Display

All badges may be requested for retina display. All that is needed is the `@2x` on the file name:

	http://cocoapod-badges.herokuapp.com/v/$PODNAME/badge@2x.(png|svg)
	
	http://cocoapod-badges.herokuapp.com/p/$PODNAME/badge@2x.(png|svg)

## Version Badge

Displays the pod's latest version available.

	http://cocoapod-badges.herokuapp.com/v/$PODNAME/badge.(png|svg)

[![NSStringMask](http://cocoapod-badges.herokuapp.com/v/NSStringMask/badge.png)](http://cocoadocs.org/docsets/NSStringMask)

Some folks were having trouble with Github's cache for the README file, so I enabled a URL parameter to set the version manually.

	http://cocoapod-badges.herokuapp.com/v/$PODNAME/$VERSION/badge.(png|svg)

[![NSStringMask](http://cocoapod-badges.herokuapp.com/v/NSStringMask/$VERSION/badge.png)](http://cocoadocs.org/docsets/NSStringMask)

| type | 1.0 | 1.1.2 | 1.0-RC1 | error |
|------|-----|-------|---------|-------|
| SVG | ![ios](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0/badge.svg) | ![osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.1.2/badge.svg) | ![ios/osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0-RC1/badge.svg) | ![error](http://cocoapod-badges.herokuapp.com/v/error/badge.svg) |
| PNG | ![ios](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0/badge.png) | ![osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.1.2/badge.png) | ![ios/osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0-RC1/badge.png) | ![error](http://cocoapod-badges.herokuapp.com/v/error/badge.png) |
| **RETINA** |
| SVG | ![ios](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0/badge@2x.svg) | ![osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.1.2/badge@2x.svg) | ![ios/osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0-RC1/badge@2x.svg) | ![error](http://cocoapod-badges.herokuapp.com/v/error/badge@2x.svg) |
| PNG | ![ios](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0/badge@2x.png) | ![osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.1.2/badge@2x.png) | ![ios/osx](http://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0-RC1/badge@2x.png) | ![error](http://cocoapod-badges.herokuapp.com/v/error/badge@2x.png) |

## Platforms Badge

For the platform info to be available, the pod must provide this in the Podspec, but it's optional. If the platform not set, the badge will display "error", even though `$PODNAME` may be correct! You can also choose between displaying an SVG and PNG.

	http://cocoapod-badges.herokuapp.com/p/$PODNAME/badge.(png|svg)

| type | iOS | OSX | iOS/OSX | error
|------|-----|-----|---------|-------|
| SVG | ![ios](http://cocoapod-badges.herokuapp.com/p/AKLocationManager/badge.svg) | ![osx](http://cocoapod-badges.herokuapp.com/p/DDQuicklookAdditionalViews/badge.svg) | ![ios/osx](http://cocoapod-badges.herokuapp.com/p/AFNetworking/badge.svg) | ![error](http://cocoapod-badges.herokuapp.com/p/error/badge.svg) |
| PNG | ![ios](http://cocoapod-badges.herokuapp.com/p/AKLocationManager/badge.png) | ![osx](http://cocoapod-badges.herokuapp.com/p/DDQuicklookAdditionalViews/badge.png) | ![ios/osx](http://cocoapod-badges.herokuapp.com/p/AFNetworking/badge.png) | ![error](http://cocoapod-badges.herokuapp.com/p/error/badge.png) |
| **RETINA** |
| SVG | ![ios](http://cocoapod-badges.herokuapp.com/p/AKLocationManager/badge@2x.svg) | ![osx](http://cocoapod-badges.herokuapp.com/p/DDQuicklookAdditionalViews/badge@2x.svg) | ![ios/osx](http://cocoapod-badges.herokuapp.com/p/AFNetworking/badge@2x.svg) | ![error](http://cocoapod-badges.herokuapp.com/p/error/badge@2x.svg) |
| PNG | ![ios](http://cocoapod-badges.herokuapp.com/p/NSStringMask/1.0/badge@2x.png) | ![osx](http://cocoapod-badges.herokuapp.com/p/DDQuicklookAdditionalViews/badge@2x.png) | ![ios/osx](http://cocoapod-badges.herokuapp.com/p/AFNetworking/badge@2x.png) | ![error](http://cocoapod-badges.herokuapp.com/p/error/badge@2x.png) |

# License

cocoapod-badges is licensed under the MIT License:

Copyright (c) 2013 Flávio Caetano ([http://flaviocaetano.com](http://flaviocaetano.com))

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[Cocoapods]: http://cocoapods.org
