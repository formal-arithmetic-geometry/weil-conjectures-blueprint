+++
kind  = "proof"
of    = "lem-weil-pbc-derived-open-restriction"
+++
For an etale $W\to U$, also viewed as etale over $S$, the direct
image of [def-weil-pbc-direct-image] satisfies

$$
(a^{-1}f_*F)(W)=F(T\times_SW)
=(f_{U,*}b^{-1}F)(W).
$$

Here restriction along an open is the inverse image of
[def-weil-pbc-inverse-image], which is exact by
[prop-weil-pbc-inverse-image-exact]. The extension-by-zero functor
$b_!$ of [def-weil-pbc-extension-by-zero] is exact and left
adjoint to $b^{-1}$. Consequently, if $I$ is injective on
$T_{\Et}$, the identity

$$
\operatorname{Hom}_{V_{\Et}}(-,b^{-1}I)
\simeq \operatorname{Hom}_{T_{\Et}}(b_!(-),I)
$$

is an exact contravariant functor: $b_!$ preserves short exact
sequences, and $\operatorname{Hom}(-,I)$ is exact. Thus $b^{-1}I$
is injective.

Choose a bounded-below injective resolution $L\to I^\bullet$ as in
[prop-weil-pbc-kinjective-resolutions-exist]. Exactness of
$b^{-1}$ and the preceding injectivity calculation make
$b^{-1}I^\bullet$ an injective resolution of $b^{-1}L$.
The displayed identity of sections applied in every degree identifies
$a^{-1}f_*I^\bullet$ with $f_{U,*}b^{-1}I^\bullet$.
Since $a^{-1}$ is exact, these represent the two derived functors
in the statement. This proves the derived isomorphism.
These identifications are restrictions of the same sections, so they
commute with successive restrictions and composition of direct images.
