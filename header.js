var globalObject = {};
var navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    platform: "Win32",
    product: "Gecko",
    productSub: "20030107",
    language: (Date.parse(new Date())/1000).toString(),
    languages: ["zh", 'zh-CN'],
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    getOwnPropertyDescriptor: function name(params) {
        return undefined
    },
    cpuClass: null,
    doNotTrack: null,
    plugins: [{
        0: {
            type: 'application/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        1: {type: 'text/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        "application/pdf": {
            type: 'application/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        "text/pdf": {
            type: 'text/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        name: 'Chrome PDF Viewer',
        filename: 'internal-pdf-viewer',
        description: 'Portable Document Format'
    }, {
        0: {type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        1: {type: 'text/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        "application/pdf": {
            type: 'application/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        "text/pdf": {
            type: 'text/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        name: 'Chromium PDF Viewer',
        filename: 'internal-pdf-viewer',
        description: 'Portable Document Format'
    }, {
        0: {type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        1: {type: 'text/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        "application/pdf": {
            type: 'application/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        "text/pdf": {
            type: 'text/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        name: 'Microsoft Edge PDF Viewer',
        filename: 'internal-pdf-viewer',
        description: 'Portable Document Format'
    }, {
        0: {type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        1: {type: 'text/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        "application/pdf": {
            type: 'application/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        "text/pdf": {
            type: 'text/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        name: 'PDF Viewer',
        filename: 'internal-pdf-viewer',
        description: 'Portable Document Format'
    }, {
        0: {type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        1: {type: 'text/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: "Plugin"},
        "application/pdf": {
            type: 'application/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        "text/pdf": {
            type: 'text/pdf',
            suffixes: 'pdf',
            description: 'Portable Document Format',
            enabledPlugin: "Plugin"
        },
        name: 'WebKit built-in PDF',
        filename: 'internal-pdf-viewer',
        description: 'Portable Document Format'
    }],
};
var localStorage = {
    length: 0, getItem: function name(params) {
    }
};
var canvas = {
    style: {display: undefined}, height: 160, width: 600, title: '', lang: '', getContext: function name(params) {
        if (params == "2d") {
            return CanvasRenderingContext2D
        }
    }, toDataURL: function name(params) {
        return 'data:image/webp;base64,UklGRmACAABXRUJQVlA4WAoAAAAwAAAAAAAAAAAASUNDUBgCAAAAAAIYAAAAAAQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAAHRyWFlaAAABZAAAABRnWFlaAAABeAAAABRiWFlaAAABjAAAABRyVFJDAAABoAAAAChnVFJDAAABoAAAAChiVFJDAAABoAAAACh3dHB0AAAByAAAABRjcHJ0AAAB3AAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAFgAAAAcAHMAUgBHAEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhZWiAAAAAAAABvogAAOPUAAAOQWFlaIAAAAAAAAGKZAAC3hQAAGNpYWVogAAAAAAAAJKAAAA+EAAC2z3BhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABYWVogAAAAAAAA9tYAAQAAAADTLW1sdWMAAAAAAAAAAQAAAAxlblVTAAAAIAAAABwARwBvAG8AZwBsAGUAIABJAG4AYwAuACAAMgAwADEANkFMUEgCAAAAAABWUDggGAAAADABAJ0BKgEAAQABQCYlpAADcAD+/TZoAA=='
    }
};
var audio = {};
var CanvasRenderingContext2D = {
    direction: "ltr",
    fillStyle: "#000000",
    filter: "none",
    font: "10px sans-serif",
    fontKerning: "auto",
    fontStretch: "normal",
    fontVariantCaps: "normal",
    globalAlpha: 1,
    globalCompositeOperation: "source-over",
    imageSmoothingEnabled: true,
    imageSmoothingQuality: "low",
    letterSpacing: "0px",
    lineCap: "butt",
    lineDashOffset: 0,
    lineJoin: "miter",
    lineWidth: 1,
    miterLimit: 10,
    shadowBlur: 0,
    shadowColor: "rgba(0, 0, 0, 0)",
    shadowOffsetX: 0,
    shadowOffsetY: 0,
    strokeStyle: "#000000",
    textAlign: "start",
    textBaseline: "alphabetic",
    textRendering: "auto",
    wordSpacing: "0px",
    isPointInPath: function name(params) {
        return false
    },
    fillRect: function name(params) {
    },
    fillText: function name(params) {
    },
    measureText: function name(params) {
    },
    rect: function name(params, p2, p3, p4) {
    },
    fillStyle: function name(params) {
    },
};
var location = {
    hash: "",
    host: "www.datasheets.com",
    hostname: "www.datasheets.com",
    href: "https://www.datasheets.com/en",
    origin: "https://www.datasheets.com",
    pathname: "/en",
    port: "",
    protocol: "https:",
    search: "?CWUDNSAI=23&xinfo=6-63536302-0%20sNNN%20RT%281661244675738%202684%29%20q%280%20-1%20-1%20-1%29%20r%280%20-1%29%20B15%2814%2c0%2c0%29%20U18&incident_id=517000390221565252-327680956469414342&edet=15&cinfo=0e000000dedd&rpinfo=649&mth=GET"
};
var currentscript = {
    getAttribute: function name(params) {
        return "https://www.datasheets.com/ckly-was-is-go-theere-my-Iewes-neede-worth-And-h"
    }, src: "https://www.datasheets.com/ckly-was-is-go-theere-my-Iewes-neede-worth-And-h"
};
var document = {
    readyState: "interactive",
    body: {
        addBehavior: false, insertBefore_e421bb29: {}, __proto__: {
            insertBefore: function name(params) {
            }
        }
    },
    createElement: function name(params) {
        if (params == "IFRAME") {
            return iframe
        }
        if (params == "canvas") {
            return canvas
        }
        if (params == "audio") {
            return audio
        }
    },
    getElementsByTagName: function name(params) {
        if (params == 'script') {
            return [currentscript]
        }
    },
    addEventListener: function name(params, params1) {
    },
    cookie: "herecookies",
    location: location
};
var window = {
    clearTimeout: clearTimeout,
    setTimeout: setTimeout,
    Object: {
        getOwnPropertyNames: function name(params) {
            return ["0", "1", "Object", "Function", "Array", "Number", "parseFloat", "parseInt", "Infinity", "NaN", "undefined", "Boolean", "String", "Symbol", "Date", "Promise", "RegExp", "Error", "AggregateError", "EvalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "globalThis", "JSON", "Math", "console", "Intl", "ArrayBuffer", "Uint8Array", "Int8Array", "Uint16Array", "Int16Array", "Uint32Array", "Int32Array", "Float32Array", "Float64Array", "Uint8ClampedArray", "BigUint64Array", "BigInt64Array", "DataView", "Map", "BigInt", "Set", "WeakMap", "WeakSet", "Proxy", "Reflect", "FinalizationRegistry", "WeakRef", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "escape", "unescape", "eval", "isFinite", "isNaN", "Option", "Image", "Audio", "webkitURL", "webkitRTCPeerConnection", "webkitMediaStream", "WebKitMutationObserver", "WebKitCSSMatrix", "XPathResult", "XPathExpression", "XPathEvaluator", "XMLSerializer", "XMLHttpRequestUpload", "XMLHttpRequestEventTarget", "XMLHttpRequest", "XMLDocument", "WritableStreamDefaultWriter", "WritableStreamDefaultController", "WritableStream", "Worker", "Window", "WheelEvent", "WebSocket", "WebGLVertexArrayObject", "WebGLUniformLocation", "WebGLTransformFeedback", "WebGLTexture", "WebGLSync", "WebGLShaderPrecisionFormat", "WebGLShader", "WebGLSampler", "WebGLRenderingContext", "WebGLRenderbuffer", "WebGLQuery", "WebGLProgram", "WebGLFramebuffer", "WebGLContextEvent", "WebGLBuffer", "WebGLActiveInfo", "WebGL2RenderingContext", "WaveShaperNode", "VisualViewport", "ValidityState", "VTTCue", "UserActivation", "URLSearchParams", "URL", "UIEvent", "TreeWalker", "TransitionEvent", "TransformStream", "TrackEvent", "TouchList", "TouchEvent", "Touch", "TimeRanges", "TextTrackList", "TextTrackCueList", "TextTrackCue", "TextTrack", "TextMetrics", "TextEvent", "TextEncoderStream", "TextEncoder", "TextDecoderStream", "TextDecoder", "Text", "TaskAttributionTiming", "SyncManager", "SubmitEvent", "StyleSheetList", "StyleSheet", "StylePropertyMapReadOnly", "StylePropertyMap", "StorageEvent", "Storage", "StereoPannerNode", "StaticRange", "ShadowRoot", "Selection", "SecurityPolicyViolationEvent", "ScriptProcessorNode", "ScreenOrientation", "Screen", "SVGViewElement", "SVGUseElement", "SVGUnitTypes", "SVGTransformList", "SVGTransform", "SVGTitleElement", "SVGTextPositioningElement", "SVGTextPathElement", "SVGTextElement", "SVGTextContentElement", "SVGTSpanElement", "SVGSymbolElement", "SVGSwitchElement", "SVGStyleElement", "SVGStringList", "SVGStopElement", "SVGSetElement", "SVGScriptElement", "SVGSVGElement", "SVGRectElement", "SVGRect", "SVGRadialGradientElement", "SVGPreserveAspectRatio", "SVGPolylineElement", "SVGPolygonElement", "SVGPointList", "SVGPoint", "SVGPatternElement", "SVGPathElement", "SVGNumberList", "SVGNumber", "SVGMetadataElement", "SVGMatrix", "SVGMaskElement", "SVGMarkerElement", "SVGMPathElement", "SVGLinearGradientElement", "SVGLineElement", "SVGLengthList", "SVGLength", "SVGImageElement", "SVGGraphicsElement", "SVGGradientElement", "SVGGeometryElement", "SVGGElement", "SVGForeignObjectElement", "SVGFilterElement", "SVGFETurbulenceElement", "SVGFETileElement", "SVGFESpotLightElement", "SVGFESpecularLightingElement", "SVGFEPointLightElement", "SVGFEOffsetElement", "SVGFEMorphologyElement", "SVGFEMergeNodeElement", "SVGFEMergeElement", "SVGFEImageElement", "SVGFEGaussianBlurElement", "SVGFEFuncRElement", "SVGFEFuncGElement", "SVGFEFuncBElement", "SVGFEFuncAElement", "SVGFEFloodElement", "SVGFEDropShadowElement", "SVGFEDistantLightElement", "SVGFEDisplacementMapElement", "SVGFEDiffuseLightingElement", "SVGFEConvolveMatrixElement", "SVGFECompositeElement", "SVGFEComponentTransferElement", "SVGFEColorMatrixElement", "SVGFEBlendElement", "SVGEllipseElement", "SVGElement", "SVGDescElement", "SVGDefsElement", "SVGComponentTransferFunctionElement", "SVGClipPathElement", "SVGCircleElement", "SVGAnimationElement", "SVGAnimatedTransformList", "SVGAnimatedString", "SVGAnimatedRect", "SVGAnimatedPreserveAspectRatio", "SVGAnimatedNumberList", "SVGAnimatedNumber", "SVGAnimatedLengthList", "SVGAnimatedLength", "SVGAnimatedInteger", "SVGAnimatedEnumeration", "SVGAnimatedBoolean", "SVGAnimatedAngle", "SVGAnimateTransformElement", "SVGAnimateMotionElement", "SVGAnimateElement", "SVGAngle", "SVGAElement", "Response", "ResizeObserverSize", "ResizeObserverEntry", "ResizeObserver", "Request", "ReportingObserver", "ReadableStreamDefaultReader", "ReadableStreamDefaultController", "ReadableStreamBYOBRequest", "ReadableStreamBYOBReader", "ReadableStream", "ReadableByteStreamController", "Range", "RadioNodeList", "RTCTrackEvent", "RTCStatsReport", "RTCSessionDescription", "RTCSctpTransport", "RTCRtpTransceiver", "RTCRtpSender", "RTCRtpReceiver", "RTCPeerConnectionIceEvent", "RTCPeerConnectionIceErrorEvent", "RTCPeerConnection", "RTCIceCandidate", "RTCErrorEvent", "RTCError", "RTCEncodedVideoFrame", "RTCEncodedAudioFrame", "RTCDtlsTransport", "RTCDataChannelEvent", "RTCDataChannel", "RTCDTMFToneChangeEvent", "RTCDTMFSender", "RTCCertificate", "PromiseRejectionEvent", "ProgressEvent", "ProcessingInstruction", "PopStateEvent", "PointerEvent", "PluginArray", "Plugin", "PeriodicWave", "PerformanceTiming", "PerformanceServerTiming", "PerformanceResourceTiming", "PerformancePaintTiming", "PerformanceObserverEntryList", "PerformanceObserver", "PerformanceNavigationTiming", "PerformanceNavigation", "PerformanceMeasure", "PerformanceMark", "PerformanceLongTaskTiming", "PerformanceEventTiming", "PerformanceEntry", "PerformanceElementTiming", "Performance", "Path2D", "PannerNode", "PageTransitionEvent", "OverconstrainedError", "OscillatorNode", "OffscreenCanvasRenderingContext2D", "OffscreenCanvas", "OfflineAudioContext", "OfflineAudioCompletionEvent", "NodeList", "NodeIterator", "NodeFilter", "Node", "NetworkInformation", "Navigator", "NamedNodeMap", "MutationRecord", "MutationObserver", "MutationEvent", "MouseEvent", "MimeTypeArray", "MimeType", "MessagePort", "MessageEvent", "MessageChannel", "MediaStreamTrackEvent", "MediaStreamTrack", "MediaStreamEvent", "MediaStreamAudioSourceNode", "MediaStreamAudioDestinationNode", "MediaStream", "MediaRecorder", "MediaQueryListEvent", "MediaQueryList", "MediaList", "MediaError", "MediaEncryptedEvent", "MediaElementAudioSourceNode", "MediaCapabilities", "Location", "LayoutShiftAttribution", "LayoutShift", "LargestContentfulPaint", "KeyframeEffect", "KeyboardEvent", "IntersectionObserverEntry", "IntersectionObserver", "InputEvent", "InputDeviceInfo", "InputDeviceCapabilities", "ImageData", "ImageCapture", "ImageBitmapRenderingContext", "ImageBitmap", "IdleDeadline", "IIRFilterNode", "IDBVersionChangeEvent", "IDBTransaction", "IDBRequest", "IDBOpenDBRequest", "IDBObjectStore", "IDBKeyRange", "IDBIndex", "IDBFactory", "IDBDatabase", "IDBCursorWithValue", "IDBCursor", "History", "Headers", "HashChangeEvent", "HTMLVideoElement", "HTMLUnknownElement", "HTMLUListElement", "HTMLTrackElement", "HTMLTitleElement", "HTMLTimeElement", "HTMLTextAreaElement", "HTMLTemplateElement", "HTMLTableSectionElement", "HTMLTableRowElement", "HTMLTableElement", "HTMLTableColElement", "HTMLTableCellElement", "HTMLTableCaptionElement", "HTMLStyleElement", "HTMLSpanElement", "HTMLSourceElement", "HTMLSlotElement", "HTMLSelectElement", "HTMLScriptElement", "HTMLQuoteElement", "HTMLProgressElement", "HTMLPreElement", "HTMLPictureElement", "HTMLParamElement", "HTMLParagraphElement", "HTMLOutputElement", "HTMLOptionsCollection", "HTMLOptionElement", "HTMLOptGroupElement", "HTMLObjectElement", "HTMLOListElement", "HTMLModElement", "HTMLMeterElement", "HTMLMetaElement", "HTMLMenuElement", "HTMLMediaElement", "HTMLMarqueeElement", "HTMLMapElement", "HTMLLinkElement", "HTMLLegendElement", "HTMLLabelElement", "HTMLLIElement", "HTMLInputElement", "HTMLImageElement", "HTMLIFrameElement", "HTMLHtmlElement", "HTMLHeadingElement", "HTMLHeadElement", "HTMLHRElement", "HTMLFrameSetElement", "HTMLFrameElement", "HTMLFormElement", "HTMLFormControlsCollection", "HTMLFontElement", "HTMLFieldSetElement", "HTMLEmbedElement", "HTMLElement", "HTMLDocument", "HTMLDivElement", "HTMLDirectoryElement", "HTMLDialogElement", "HTMLDetailsElement", "HTMLDataListElement", "HTMLDataElement", "HTMLDListElement", "HTMLCollection", "HTMLCanvasElement", "HTMLButtonElement", "HTMLBodyElement", "HTMLBaseElement", "HTMLBRElement", "HTMLAudioElement", "HTMLAreaElement", "HTMLAnchorElement", "HTMLAllCollection", "GeolocationPositionError", "GeolocationPosition", "GeolocationCoordinates", "Geolocation", "GamepadHapticActuator", "GamepadEvent", "GamepadButton", "Gamepad", "GainNode", "FormDataEvent", "FormData", "FontFaceSetLoadEvent", "FontFace", "FocusEvent", "FileReader", "FileList", "File", "FeaturePolicy", "External", "EventTarget", "EventSource", "EventCounts", "Event", "ErrorEvent", "ElementInternals", "Element", "DynamicsCompressorNode", "DragEvent", "DocumentType", "DocumentFragment", "Document", "DelayNode", "DecompressionStream", "DataTransferItemList", "DataTransferItem", "DataTransfer", "DOMTokenList", "DOMStringMap", "DOMStringList", "DOMRectReadOnly", "DOMRectList", "DOMRect", "DOMQuad", "DOMPointReadOnly", "DOMPoint", "DOMParser", "DOMMatrixReadOnly", "DOMMatrix", "DOMImplementation", "DOMException", "DOMError", "CustomEvent", "CustomElementRegistry", "Crypto", "CountQueuingStrategy", "ConvolverNode", "ConstantSourceNode", "CompressionStream", "CompositionEvent", "Comment", "CloseEvent", "ClipboardEvent", "CharacterData", "ChannelSplitterNode", "ChannelMergerNode", "CanvasRenderingContext2D", "CanvasPattern", "CanvasGradient", "CanvasCaptureMediaStreamTrack", "CSSVariableReferenceValue", "CSSUnparsedValue", "CSSUnitValue", "CSSTranslate", "CSSTransformValue", "CSSTransformComponent", "CSSSupportsRule", "CSSStyleValue", "CSSStyleSheet", "CSSStyleRule", "CSSStyleDeclaration", "CSSSkewY", "CSSSkewX", "CSSSkew", "CSSScale", "CSSRuleList", "CSSRule", "CSSRotate", "CSSPropertyRule", "CSSPositionValue", "CSSPerspective", "CSSPageRule", "CSSNumericValue", "CSSNumericArray", "CSSNamespaceRule", "CSSMediaRule", "CSSMatrixComponent", "CSSMathValue", "CSSMathSum", "CSSMathProduct", "CSSMathNegate", "CSSMathMin", "CSSMathMax", "CSSMathInvert", "CSSKeywordValue", "CSSKeyframesRule", "CSSKeyframeRule", "CSSImportRule", "CSSImageValue", "CSSGroupingRule", "CSSFontFaceRule", "CSSCounterStyleRule", "CSSConditionRule", "CSS", "CDATASection", "ByteLengthQueuingStrategy", "BroadcastChannel", "BlobEvent", "Blob", "BiquadFilterNode", "BeforeUnloadEvent", "BeforeInstallPromptEvent", "BatteryManager", "BaseAudioContext", "BarProp", "AudioWorkletNode", "AudioScheduledSourceNode", "AudioProcessingEvent", "AudioParamMap", "AudioParam", "AudioNode", "AudioListener", "AudioDestinationNode", "AudioContext", "AudioBufferSourceNode", "AudioBuffer", "Attr", "AnimationEvent", "AnimationEffect", "Animation", "AnalyserNode", "AbstractRange", "AbortSignal", "AbortController", "window", "self", "document", "name", "location", "customElements", "history", "locationbar", "menubar", "personalbar", "scrollbars", "statusbar", "toolbar", "status", "closed", "frames", "length", "top", "opener", "parent", "frameElement", "navigator", "origin", "external", "screen", "innerWidth", "innerHeight", "scrollX", "pageXOffset", "scrollY", "pageYOffset", "visualViewport", "screenX", "screenY", "outerWidth", "outerHeight", "devicePixelRatio", "event", "clientInformation", "offscreenBuffering", "screenLeft", "screenTop", "defaultStatus", "defaultstatus", "styleMedia", "onsearch", "isSecureContext", "performance", "onappinstalled", "onbeforeinstallprompt", "crypto", "indexedDB", "webkitStorageInfo", "sessionStorage", "localStorage", "onbeforexrselect", "onabort", "onblur", "oncancel", "oncanplay", "oncanplaythrough", "onchange", "onclick", "onclose", "oncontextmenu", "oncuechange", "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragleave", "ondragover", "ondragstart", "ondrop", "ondurationchange", "onemptied", "onended", "onerror", "onfocus", "onformdata", "oninput", "oninvalid", "onkeydown", "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata", "onloadstart", "onmousedown", "onmouseenter", "onmouseleave", "onmousemove", "onmouseout", "onmouseover", "onmouseup", "onmousewheel", "onpause", "onplay", "onplaying", "onprogress", "onratechange", "onreset", "onresize", "onscroll", "onsecuritypolicyviolation", "onseeked", "onseeking", "onselect", "onslotchange", "onstalled", "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "onvolumechange", "onwaiting", "onwebkitanimationend", "onwebkitanimationiteration", "onwebkitanimationstart", "onwebkittransitionend", "onwheel", "onauxclick", "ongotpointercapture", "onlostpointercapture", "onpointerdown", "onpointermove", "onpointerup", "onpointercancel", "onpointerover", "onpointerout", "onpointerenter", "onpointerleave", "onselectstart", "onselectionchange", "onanimationend", "onanimationiteration", "onanimationstart", "ontransitionrun", "ontransitionstart", "ontransitionend", "ontransitioncancel", "onafterprint", "onbeforeprint", "onbeforeunload", "onhashchange", "onlanguagechange", "onmessage", "onmessageerror", "onoffline", "ononline", "onpagehide", "onpageshow", "onpopstate", "onrejectionhandled", "onstorage", "onunhandledrejection", "onunload", "alert", "atob", "blur", "btoa", "cancelAnimationFrame", "cancelIdleCallback", "captureEvents", "clearInterval", "clearTimeout", "close", "confirm", "createImageBitmap", "fetch", "find", "focus", "getComputedStyle", "getSelection", "matchMedia", "moveBy", "moveTo", "open", "postMessage", "print", "prompt", "queueMicrotask", "releaseEvents", "reportError", "requestAnimationFrame", "requestIdleCallback", "resizeBy", "resizeTo", "scroll", "scrollBy", "scrollTo", "setInterval", "setTimeout", "stop", "structuredClone", "webkitCancelAnimationFrame", "webkitRequestAnimationFrame", "Atomics", "chrome", "WebAssembly", "caches", "cookieStore", "ondevicemotion", "ondeviceorientation", "ondeviceorientationabsolute", "oncontextlost", "oncontextrestored", "AbsoluteOrientationSensor", "Accelerometer", "AudioWorklet", "Cache", "CacheStorage", "Clipboard", "ClipboardItem", "CookieChangeEvent", "CookieStore", "CookieStoreManager", "Credential", "CredentialsContainer", "CryptoKey", "DeviceMotionEvent", "DeviceMotionEventAcceleration", "DeviceMotionEventRotationRate", "DeviceOrientationEvent", "FederatedCredential", "Gyroscope", "Keyboard", "KeyboardLayoutMap", "LinearAccelerationSensor", "Lock", "LockManager", "MIDIAccess", "MIDIConnectionEvent", "MIDIInput", "MIDIInputMap", "MIDIMessageEvent", "MIDIOutput", "MIDIOutputMap", "MIDIPort", "MediaDeviceInfo", "MediaDevices", "MediaKeyMessageEvent", "MediaKeySession", "MediaKeyStatusMap", "MediaKeySystemAccess", "MediaKeys", "NavigationPreloadManager", "NavigatorManagedData", "OrientationSensor", "PasswordCredential", "RTCIceTransport", "RelativeOrientationSensor", "Sensor", "SensorErrorEvent", "ServiceWorker", "ServiceWorkerContainer", "ServiceWorkerRegistration", "StorageManager", "SubtleCrypto", "Worklet", "XRDOMOverlayState", "XRLayer", "XRWebGLBinding", "AudioData", "EncodedAudioChunk", "EncodedVideoChunk", "ImageTrack", "ImageTrackList", "VideoColorSpace", "VideoFrame", "AudioDecoder", "AudioEncoder", "ImageDecoder", "VideoDecoder", "VideoEncoder", "AuthenticatorAssertionResponse", "AuthenticatorAttestationResponse", "AuthenticatorResponse", "PublicKeyCredential", "Bluetooth", "BluetoothCharacteristicProperties", "BluetoothDevice", "BluetoothRemoteGATTCharacteristic", "BluetoothRemoteGATTDescriptor", "BluetoothRemoteGATTServer", "BluetoothRemoteGATTService", "CanvasFilter", "EyeDropper", "FileSystemDirectoryHandle", "FileSystemFileHandle", "FileSystemHandle", "FileSystemWritableFileStream", "FragmentDirective", "GravitySensor", "HID", "HIDConnectionEvent", "HIDDevice", "HIDInputReportEvent", "IdleDetector", "MediaStreamTrackGenerator", "MediaStreamTrackProcessor", "OTPCredential", "PaymentAddress", "PaymentRequest", "PaymentResponse", "PaymentMethodChangeEvent", "Presentation", "PresentationAvailability", "PresentationConnection", "PresentationConnectionAvailableEvent", "PresentationConnectionCloseEvent", "PresentationConnectionList", "PresentationReceiver", "PresentationRequest", "Profiler", "Scheduling", "Serial", "SerialPort", "USB", "USBAlternateInterface", "USBConfiguration", "USBConnectionEvent", "USBDevice", "USBEndpoint", "USBInTransferResult", "USBInterface", "USBIsochronousInTransferPacket", "USBIsochronousInTransferResult", "USBIsochronousOutTransferPacket", "USBIsochronousOutTransferResult", "USBOutTransferResult", "VirtualKeyboard", "WakeLock", "WakeLockSentinel", "WebTransport", "WebTransportBidirectionalStream", "WebTransportDatagramDuplexStream", "WebTransportError", "XRAnchor", "XRAnchorSet", "XRBoundedReferenceSpace", "XRFrame", "XRInputSource", "XRInputSourceArray", "XRInputSourceEvent", "XRInputSourcesChangeEvent", "XRPose", "XRReferenceSpace", "XRReferenceSpaceEvent", "XRRenderState", "XRRigidTransform", "XRSession", "XRSessionEvent", "XRSpace", "XRSystem", "XRView", "XRViewerPose", "XRViewport", "XRWebGLLayer", "XRCPUDepthInformation", "XRDepthInformation", "XRWebGLDepthInformation", "XRHitTestResult", "XRHitTestSource", "XRRay", "XRTransientInputHitTestResult", "XRTransientInputHitTestSource", "XRLightEstimate", "XRLightProbe", "showDirectoryPicker", "showOpenFilePicker", "showSaveFilePicker", "originAgentCluster", "trustedTypes", "speechSynthesis", "onpointerrawupdate", "crossOriginIsolated", "scheduler", "AnimationPlaybackEvent", "AnimationTimeline", "CSSAnimation", "CSSTransition", "DocumentTimeline", "BackgroundFetchManager", "BackgroundFetchRecord", "BackgroundFetchRegistration", "BluetoothUUID", "CSSLayerBlockRule", "CSSLayerStatementRule", "CustomStateSet", "DelegatedInkTrailPresenter", "Ink", "MediaMetadata", "MediaSession", "MediaSource", "SourceBuffer", "SourceBufferList", "NavigatorUAData", "Notification", "PaymentInstruments", "PaymentManager", "PaymentRequestUpdateEvent", "PeriodicSyncManager", "PermissionStatus", "Permissions", "PictureInPictureEvent", "PictureInPictureWindow", "PushManager", "PushSubscription", "PushSubscriptionOptions", "RemotePlayback", "Scheduler", "TaskController", "TaskPriorityChangeEvent", "TaskSignal", "SharedWorker", "SpeechSynthesisErrorEvent", "SpeechSynthesisEvent", "SpeechSynthesisUtterance", "TrustedHTML", "TrustedScript", "TrustedScriptURL", "TrustedTypePolicy", "TrustedTypePolicyFactory", "URLPattern", "VideoPlaybackQuality", "VirtualKeyboardGeometryChangeEvent", "XSLTProcessor", "webkitSpeechGrammar", "webkitSpeechGrammarList", "webkitSpeechRecognition", "webkitSpeechRecognitionError", "webkitSpeechRecognitionEvent", "openDatabase", "webkitRequestFileSystem", "webkitResolveLocalFileSystemURL", "showBlockPage", "onProtectionInitialized", "getFrameLocation", "handler", "__VUE_DEVTOOLS_IFRAME__", "__VUE_DEVTOOLS_GLOBAL_HOOK__", "a0_0x1ec9", "a0_0x515f", "reese84", "reese84interrogator", "initializeProtection", "protectionSubmitCaptcha", "reeseRetriedAutoload", "dir", "dirxml", "profile", "profileEnd", "clear", "table", "keys", "values", "debug", "undebug", "monitor", "unmonitor", "inspect", "copy", "queryObjects", "$_", "$0", "$1", "$2", "$3", "$4", "getEventListeners", "getAccessibleName", "getAccessibleRole", "monitorEvents", "unmonitorEvents", "$", "$$", "$x"]
        }
    },
    parseInt: parseInt,
    PERSISTENT: 1,
    history: {length: 2, scrollRestoration: "auto", state: null,},
    startInternal: function name(params) {
    },
    stopInternal: function name(params) {
    },
    Math: Math,
    start: function name(params) {
    },
    JSON: JSON,
    Array: Array,
    "Math": Math,
    "contentWindow": "contentWindow",
    "contentDocument": "contentDocument",
    "screen": {
        availHeight: 1040,
        availLeft: -1920,
        availTop: 144,
        availWidth: 1920,
        colorDepth: 24,
        height: 1080,
        pixelDepth: 24,
        width: 1920,
        orientation: {type: "landscape-primary"}
    },
    "innerWidth": 150,
    "innerHeight": 937,
    "outerWidth": 1912,
    outerHeight: 1032,
    devicePixelRatio: 1,
    screenLeft: -1916,
    screenTop: 148,
    screenX: -1916,
    screenY: 148,
    Date: Date,
    indexedDB: "indexedDB",
    openDatabase: "openDatabase",
    btoa: btoa,
    atob: atob,
    String: String,
    RegExp: RegExp,
    fetch: {
        bind: function name(params) {
        }
    },
    navigator: navigator,
    location: location,
    document: document,
};
var iframe = {
    style: {display: undefined},
    addEventListener: function name(params, params1) {
        params1()
    },
    contentWindow: window,
    contentDocument: document,
    parentNode: {
        baseRemoveChild_e421bb29: '', __proto__: {
            removeChild: function name(params) {
            }
        }
    }
};
global['window'] = window;