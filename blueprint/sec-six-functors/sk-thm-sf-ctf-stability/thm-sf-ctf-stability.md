+++
id = "thm-sf-ctf-stability"
kind = "theorem"
title = "Preservation on the proved finite-Tor domains"
order = 2517
uses = ["cor-coef-finite-verdier", "cor-pur-general-admissibility-datum", "cor-pur-smooth-admissibility", "cor-coef-integral-internal-hom", "cor-sf-direct-image-ctf-proetale", "cor-sf-hom-ctf-proetale-unconditional", "cor-weil-finite-constructible-hom", "def-compact-support-direct-image-detailed", "def-weil-derived-complete-integral-detailed", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "def-weil-site-perfect-complex", "lem-coef-finite-direct-image", "lem-coef-finite-exceptional", "lem-coef-integral-hom-reduction", "lem-coef-integral-residue-tor", "lem-coef-rational-operations", "lem-exc-constant-inverse-image-flat", "lem-fix-operation-reduction", "lem-sf-etale-direct-image-vanishing", "lem-weil-pbc-pullback-preserves-bounded-constructible", "prop-coef-integral-exceptional-adjoint", "prop-exc-closed-tor", "prop-sf-dualizable-hom", "thm-coef-finite-hom", "thm-coef-integral-verdier", "thm-coef-qbar-verdier", "thm-coef-rational-verdier", "thm-fix-general-biduality", "thm-pur-general-admissibility", "thm-pur-open-complement-unconditional", "thm-sf-direct-image-tor-amplitude", "thm-sf-hom-ctf", "thm-sf-preservation-class"]
+++
Fix the finite-field datum,
$A=A_{E,n}$, and separated finite-type morphisms between separated finite-type
$k$-schemes. Use the bounded
constructible categories and their
finite-Tor subcategories.
At this finite coefficient stage the following hold:

1. **(i)** $Lf^*$ carries $D^b_{ctf}(Y,A)$ into
$D^b_{ctf}(X,A)$.
1. **(ii)** Derived tensor carries
$D^b_{ctf}\times D^b_{ctf}$ into $D^b_{ctf}$; if the two inputs have
Tor amplitude in $[a,b]$ and $[c,d]$, the output has Tor amplitude in
$[a+c,b+d]$.
For $K,L\in D^b_{ctf}(X,A)$, internal Hom has this same conclusion.
If $K,L$ have Tor amplitude in $[a,b]$ and $[c,d]$ and
$\dim X\leq m$, then $R\mathcal Hom(K,L)$ has Tor amplitude in
$[c-b-2m,d-a+2m]$; if moreover $K$ is site-perfect, it has Tor
amplitude in the sharper interval $[c-b,d-a]$.
The elementary formula $R\mathcal Hom(K,L)=K^\vee\otimes^L L$, with
coefficient dual $K^\vee=R\mathcal Hom(K,A_X)$, and the dimension-free
interval $[c-b,d-a]$ require a site-perfect first argument: for the origin
$i:\{0\}\hookrightarrow\mathbf A^1$ both $i_*A$ and $A$ have Tor amplitude
$[0,0]$, while $R\mathcal Hom(i_*A,A)=i_*A(-1)[-2]$ has cohomology in
degree $2$.
1. **(iii)** $Rf_*$ carries $D^b_{ctf}(X,A)$ into
$D^b_{ctf}(Y,A)$; for input Tor amplitude $[a,b]$ and
$\dim X\leq d$, the output has Tor amplitude in $[a,b+2d]$.
1. **(iv)** $Rf_!$ carries $D^b_{ctf}(X,A)$ into
$D^b_{ctf}(Y,A)$.
1. **(v)** The exceptional adjoint on the constructible
coefficient category satisfies $Rf^!=D_Xf^*D_Y$ and carries
$D^b_{ctf}(Y,A)$ into $D^b_{ctf}(X,A)$.
For input Tor interval $[a,b]$, one output interval is
$[a-2\dim X,b+2\dim Y]$.
1. **(vi)** For every separated finite-type $X/k$,
$D_X=R\mathcal Hom_X(-,Ra_X^!A)$ is a contravariant exact
anti-equivalence with $K\simeq D_XD_XK$.
1. **(vii)** On the finite-Tor constructible domains,
finite coefficient quotients commute with pullback, tensor, both
direct images, general internal Hom, Verdier duality and the
exceptional adjoint, preserving their evaluation and adjunction maps.
For derived-complete
integral objects, $D^b_c(X,\mathcal O_E)=D^b_{ctf}(X,\mathcal O_E)$.
General internal Hom and the exceptional adjoint preserve this
category; Verdier duality is an anti-equivalence on it, with the
canonical finite reductions of these operations. These conclusions
pass to the bounded constructible categories at $E$ and
$\Qlb$, with their specified coefficient-passage operations.
