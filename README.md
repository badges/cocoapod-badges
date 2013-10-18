Cocoapod Badges ![License MIT](https://go-shields.herokuapp.com/license-MIT-blue.png)
===============

[![Badge w/ Version](https://cocoapod-badges.herokuapp.com/v/NSStringMask/badge.png)](https://cocoadocs.org/docsets/NSStringMask)
[![Badge w/ Platform](https://cocoapod-badges.herokuapp.com/p/NSStringMask/badge.svg)](https://cocoadocs.org/docsets/NSStringMask)

Cocoapod Badges are status badges to inform a pod's latest version deployed to [Cocoapods] through their [simple API](https://github.com/CocoaPods/cocoapods.org/commit/8ef51c7890c33ad899e8130b9e778c740c5c7f61).

The badges are created thanks to [jbowes/buckler](https://github.com/jbowes/buckler) that provides "shields-as-a-service".

The "badge service" is hosted at [Heroku](https://www.heroku.com/)

# Usage

Just replace the `$PODNAME` on the URLs and the badge will automatically fetch the info.

**_ATTENTION_**: The `$PODNAME` is case sensitive, since [Cocoapods] has differentiation! In case of unexpected issues, the badges will display "error".

Since the badge generation was "outsourced", for now, they can only be displayed as `PNG` images. However, the URL's `.svg` extension is still available for backwards compatibility, and there's no difference on the output for either extensions.

## Version Badge

Displays the pod's latest version available.

	http://cocoapod-badges.herokuapp.com/v/$PODNAME/badge.png

[![NSStringMask](https://cocoapod-badges.herokuapp.com/v/NSStringMask/badge.png)](https://cocoadocs.org/docsets/NSStringMask)

Some folks were having trouble with Github's cache for the README file, so I enabled a URL parameter to set the version manually.

	http://cocoapod-badges.herokuapp.com/v/$PODNAME/$VERSION/badge.png

[![NSStringMask](https://cocoapod-badges.herokuapp.com/v/NSStringMask/$VERSION/badge.png)](https://cocoadocs.org/docsets/NSStringMask)

| 1.0 | 1.1.2 | 1.0-RC1 | error |
|-----|-------|---------|-------|
| ![ios](https://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0/badge.png) | ![osx](https://cocoapod-badges.herokuapp.com/v/NSStringMask/1.1.2/badge.png) | ![ios/osx](https://cocoapod-badges.herokuapp.com/v/NSStringMask/1.0-RC1/badge.png) | ![error](https://cocoapod-badges.herokuapp.com/v/error/badge.png) |

## Platforms Badge

The Platform info is optional and it may not be set in the pod's Podspec. Be sure to correctly provide this information or the badge will not work! If there's no platform info, the badge will display "error", even though `$PODNAME` may be correct!

	http://cocoapod-badges.herokuapp.com/p/$PODNAME/badge.png

| iOS | OSX | iOS/OSX | error
|-----|-----|---------|-------|
| ![ios](https://cocoapod-badges.herokuapp.com/p/AKLocationManager/badge.png) | ![osx](https://cocoapod-badges.herokuapp.com/p/DDQuicklookAdditionalViews/badge.png) | ![ios/osx](https://cocoapod-badges.herokuapp.com/p/AFNetworking/badge.png) | ![error](https://cocoapod-badges.herokuapp.com/p/error/badge.png) |

# License

betabadges is licensed under the MIT License:

Copyright (c) 2013 Flávio Caetano ([http://flaviocaetano.com](https://flaviocaetano.com))

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[Cocoapods]: http://cocoapods.org
