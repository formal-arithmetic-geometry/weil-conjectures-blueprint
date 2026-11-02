+++
kind  = "proof"
of    = "prop-trf-compact-support-perfectness"
+++
Let $C=R\Gamma_c(X,K)$, with compact support as in
[def-compact-support-direct-image-detailed], [def-trf-coefficient-conventions].
The finite-level constructibility theorem
[prop-finite-compact-support-constructibility] gives a bounded
complex on $\operatorname{Spec}k$ with finite cohomology modules,
using the point identification of
[def-weil-finite-coefficient-point]. This assertion alone does
not give perfectness over the finite ring $A$.

Here $A$ is an arbitrary finite commutative $\ell$-primary ring, so no
residue field of a distinguished uniformizer is available; the Tor amplitude
is bounded directly. Choose a compactification $X\xrightarrow{j}\overline X\xrightarrow{\bar a}\Spec k$
as in [def-compact-support-direct-image-detailed], so $C=R\bar a_*j_!K$, and let
$\overline X$ have dimension $d$; then $R^q\bar a_*F=0$ for $q>2d$ and every sheaf of
$A$-modules $F$ ([def-weil-full-cohomological-dimension]). For a finite
$A$-module $M$, the projection formula with a finitely presented constant coefficient
[lem-sf-projection-finite-constant], applied to $\bar a$ and $j_!K$, together with
$j_!K\otimes^L_AM_{\overline X}\cong j_!(K\otimes^L_AM_X)$, gives

$$
C\otimes_A^LM\xrightarrow{\sim}R\Gamma_c(X,K\otimes_A^LM_X).
$$

If $K$ has Tor amplitude in $[a,b]$ ([def-weil-finite-tor-amplitude]), then
$K\otimes^L_AM_X$ has cohomology sheaves in $[a,b]$, so the right side has cohomology in
$[a,b+2d]$. Derived tensor products commute with filtered colimits and every
$A$-module is a filtered colimit of finite ones, so $C$ has Tor amplitude in
$[a,b+2d]$. Together with its finite
cohomology, [lem-trf-finite-tor-amplitude-perfect] shows that
$C$ is represented by a bounded complex of finite projective
$A$-modules (finite free when $A$ is local, e.g. $A=A_{E,n}$).

For $K_{\bar x}$, the exact inverse-image property
[prop-weil-pbc-inverse-image-exact] and the finite-stalk
condition of [def-weil-finite-torsion-constructibility] give
bounded finite cohomology. The tensor-vanishing definition
[def-weil-finite-tor-amplitude] is preserved by this inverse
image, so the same module-theoretic perfectness criterion applies.
Thus both objects lie in the perfect category used for categorical
trace in [def-trf-categorical-trace].
No preservation of finite Tor amplitude by a package summary is used
in this argument.

*Recorded in advance* from chapter *The trace formula* of the source.
