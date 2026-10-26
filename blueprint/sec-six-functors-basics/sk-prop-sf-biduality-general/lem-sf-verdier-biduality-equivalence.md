+++
id = "lem-sf-verdier-biduality-equivalence"
kind = "lemma"
title = "Verdier biduality and the duality anti-equivalence"
lean = ["AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app", "AlgebraicGeometry.Etale.nonempty_iso_verdierDual_verdierDual", "AlgebraicGeometry.Etale.verdierDualEquivalence"]
order = 2834
uses = ["def-nagata-compactifiable", "thm-amb-etale-exceptional-adjoint", "def-weil-derived-pullback-tensor-hom", "def-constructible-constructible", "def-weil-finite-tor-amplitude", "lem-weil-duality-pairing", "lem-weil-verdier-preservation-strata", "thm-weil-etale-geometric-biduality"]
+++
Let $k$ be an algebraically closed field and let $\Lambda$ be a finite
commutative ring whose exponent is invertible in $k$. Let
$a:X\to\operatorname{Spec}k$ be separated, quasi-compact, locally of finite
type and compactifiable [def-nagata-compactifiable]. Put
$\omega_X=Ra^!\Lambda$, with $Ra^!$ the right adjoint of $Ra_!$
[thm-amb-etale-exceptional-adjoint], and
$\mathbb D_X=R\mathcal Hom_\Lambda(-,\omega_X)$ on $D(X_{\Et},\Lambda)$
[def-weil-derived-pullback-tensor-hom]. Let
$D^b_{ctf}(X,\Lambda)\subseteq D(X_{\Et},\Lambda)$ be the full subcategory of
bounded complexes with constructible cohomology sheaves
[def-constructible-constructible] and of finite Tor amplitude
[def-weil-finite-tor-amplitude].

1. For every $K\in D^b_{ctf}(X,\Lambda)$ the double-dual morphism
$\delta_K:K\to\mathbb D_X\mathbb D_XK$ of [lem-weil-duality-pairing] is an
isomorphism. In particular $K\cong\mathbb D_X\mathbb D_XK$.
1. $\mathbb D_X$ carries $D^b_{ctf}(X,\Lambda)$ into itself and restricts to an
equivalence
$$
\mathbb D_X:\ D^b_{ctf}(X,\Lambda)^{\mathrm{op}}\xrightarrow{\ \sim\ }D^b_{ctf}(X,\Lambda)
$$
whose quasi-inverse is again $\mathbb D_X$, with unit and counit given by the
double-dual isomorphisms $\delta$.
