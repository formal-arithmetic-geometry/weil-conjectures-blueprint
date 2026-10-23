+++
id = "sk-def-sfb-dc-setting"
kind = "definition"
title = "Setting for $D_{\\mathrm{cons}}$: schemes of finite type over a field"
order = 2580
uses = ["sk-def-nagata-sketch-data", "sk-prop-sf-open-closed-triangle"]
lean = ["AlgebraicGeometry.HasCompactification.of_isOver", "AlgebraicGeometry.ProEtale.CondensedRing.compactificationOverField"]
tags = ["sketch"]
+++
Fix a prime $\ell$ and a field $k$ of characteristic $p>0$ with $p\neq\ell$. In this
setting all schemes are separated and of finite type over $k$, and all morphisms are
morphisms of $k$-schemes. No further hypothesis is imposed. For a commutative condensed
ring $\Lambda$ ([det-def-sfb-condensed-ring]) and a scheme $X$ of the setting, write

$$
D_{\mathrm{cons}}(X,\Lambda):=D_{\mathrm{cons}}(X_{\mathrm{proét}},\Lambda_X)\subseteq D(\Mod_{\Lambda_X})
$$

for the bounded constructible derived category ([det-def-sfb-bounded-constructible]) of
module objects over $\Lambda_X=p_X^*\Lambda$ ([det-def-sfb-pulled-back-coefficients]).

Every morphism $f\colon X\to Y$ of the setting has a compactification
$c=(X\xrightarrow{\ i\ }Z\xrightarrow{\ p\ }Y)$ in the sense of [sk-def-nagata-sketch-data]:
$f=p\circ i$ with $i$ an open immersion and $p$ proper. The scheme $Z$ is again separated and of
finite type over $k$, and $i$, $p$ are $k$-morphisms, so $c$ stays inside the setting. For every
$f$ we fix one such compactification

$$
c_f=(X\xrightarrow{\ i_f\ }Z_f\xrightarrow{\ p_f\ }Y),
$$

the *chosen compactification* of $f$. It is the compactification used to define $Rf_!$ and
$Rf^!$ on $D_{\mathrm{cons}}$.
