+++
id = "thm-sf-preservation-class"
kind = "theorem"
title = "The preservation clauses of exceptional-adjoint admissibility are theorems on the coefficient class"
order = 2889
uses = ["cor-pur-general-admissibility-datum", "def-compact-support-direct-image-detailed", "def-exc-open-complement-bound", "def-pur-conventions", "def-sbc-affine-space", "def-sf-fullcd-class", "def-sf-fullcd-used-class", "def-weil-ambient-exceptional-adjoint", "def-weil-compactifications-refinements", "def-weil-constructible-intervals", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-exc-open-complement-known", "lem-sf-proetale-constructible-origin", "prop-sf-comparison-bound-zero", "thm-pur-general-admissibility", "thm-pur-open-complement-unconditional", "thm-sf-ambient-adjoint-class", "thm-sf-fullcd-class"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, the algebraic
closure $k=\Fbar$ of the finite field $k_0$ of that datum, a
separated finite-type
$k$-scheme $Y$, a finite-type $k$-scheme $X$
([def-weil-scheme-morphism-properties]), and a
separated finite-type
$k$-morphism $f:X\to Y$; the source $X$ is then a separated finite-type
$k$-scheme as well, $f$ being separated and $Y$ separated over $k$.
Cover $Y$ by finitely many affine opens
$V\subseteq Y$, and for each $V$ cover $f^{-1}(V)$ by finitely many
affine opens $U\subseteq f^{-1}(V)$; each $U\to V$ is affine of finite
type, hence exhibits $U$ as a closed subscheme of the affine space
$\mathbf A^{d_U}_V$ of [def-sbc-affine-space] for some integer
$d_U\in\mathbf Z_{\geq0}$. Put $D=\max_U d_U$. Let $A=A_{E,n}$ be a
finite coefficient ring, let $Rf_{!,n}$ be the pro-étale
compact-support direct image
attached to a
compactification of
$f$, and let

$$
Rf_n^{\times}=\nu_X^*f^{\times}R\nu_{Y,*},
$$

with $\nu_X,\nu_Y$ the comparison morphisms of
[def-weil-pbc-site-comparison-morphism], be the right adjoint of
$Rf_{!,n}$ relative to the bounded-below objects of étale origin that
[thm-sf-ambient-adjoint-class] constructs on the blueprint's coefficient
class [def-sf-fullcd-used-class] (no ambient right adjoint is asserted). Read the
exceptional inverse image
$Rf^!$ as the restriction of $Rf_n^{\times}$ to $D^b_c(Y,A)$ and to its
finite-Tor objects, and use the
constructible intervals
$D_c^{[a,b]}$ and the
finite-Tor condition. Then:

1. for all integers $a\leq b$,
$$
L\in D_c^{[a,b]}(Y,A)\quad\Longrightarrow\quad
Rf^!L\in D_c^{[a-2D,\,b+2\dim Y+1]}(X,A);
$$
1. if $K\in D^b_{ctf}(Y,A)$ has finite Tor amplitude in $[a,b]$, then
$Rf^!K$ has finite Tor amplitude in $[a-2D,b+2\dim Y+1]$; in particular
$Rf^!$ carries $D^b_{ctf}(Y,A)$ into $D^b_{ctf}(X,A)$;
1. the two constants $2D$ and $2\dim Y+1$ depend on $f$ and $Y$
alone and not on the level $n$, so that the two clauses hold at
every finite coefficient ring $A_{E,n}$, $n\geq1$, with the same
constants;
1. consequently $Rf^!$ satisfies the analogues of clauses (2) and (3) of
[def-weil-exceptional-adjoint-admissibility] at every finite coefficient
stage, with the signed constants $c_f^-=-2D$ and $c_f^+=2\dim Y+1$ of
that definition, *without* assuming clause (1) of that definition.
