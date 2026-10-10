+++
kind  = "proof"
of    = "cor-sf-direct-image-ctf-etale-origin"
+++
The morphism $f$ is of finite type, hence quasi-compact and
quasi-separated, so the comparison direct image of
[prop-weil-pbc-comparison-direct-image] gives an isomorphism

$$
\nu_Y^*Rf_{\Et,*}K'\xrightarrow{\sim}Rf_{\mathrm{proet},*}\nu_X^*K'
\cong Rf_{\mathrm{proet},*}K .
$$

By [cor-sf-direct-image-ctf-nonproper] the complex
$Rf_{\Et,*}K'$ is bounded constructible on $Y_{\Et}$ with finite Tor
amplitude in $[a,b+2d]$, and [lem-exc-comparison-tor-interval]
transfers that Tor amplitude to its pullback
$\nu_Y^*Rf_{\Et,*}K'$, which is the finite-Tor condition of
[def-weil-finite-tor-amplitude] on the pro-étale site; bounded
constructibility of that pullback is
[lem-weil-pbc-pullback-preserves-bounded-constructible]. The
identification therefore exhibits $Rf_{\mathrm{proet},*}K$ as a bounded
constructible pro-étale object of finite Tor amplitude in $[a,b+2d]$.
By [def-weil-pbc-proetale-modules] the bounded constructible
pro-étale objects are the pullbacks of the bounded constructible étale
objects, a reading recorded in clause (3) of
[lem-cbc-proetale-stalk-conservative]; for those objects the
corollary is exactly clause (iii) of the finite-Tor preservation summary at the
finite coefficient stage $A$.
