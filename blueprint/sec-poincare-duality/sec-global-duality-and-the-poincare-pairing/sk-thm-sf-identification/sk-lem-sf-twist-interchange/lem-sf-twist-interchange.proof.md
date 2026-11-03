+++
kind  = "proof"
of    = "lem-sf-twist-interchange"
+++
By [def-coefficient-twists-detailed] each $\Lambda(m)_X$ is invertible locally
constant of rank one with
$\Lambda(m)_X\otimes^L\Lambda(-m)_X\cong\Lambda_X$, so
$T_m=-\otimes^L\Lambda(m)_X$ is an exact autoequivalence with inverse
$T_{-m}$. For an invertible $N$ the canonical map
$c_{M,N}:R\mathcal H om_X(K,M)\otimes^LN\to R\mathcal H om_X(K,M\otimes^LN)$,
the tensor–Hom transpose of $\mathrm{ev}\otimes1$, is an isomorphism
directly: by the coherence of these maps,
$c_{M\otimes N,N^{-1}}\circ(c_{M,N}\otimes N^{-1})=c_{M,N\otimes N^{-1}}$ is
the identity under $N\otimes^LN^{-1}\cong\Lambda_X$, and symmetrically on
the other side, so $c_{M,N}$ has a two-sided inverse. No appeal to a
generator is made: $\Lambda_X$ does not generate $D^b_{ctf}(X,\Lambda)$, so
agreement of the two sides at $M=\Lambda_X$ would prove nothing, and
[lem-sf-generating-class-determination] is not used. For $K$ perfect the asserted map is the identification of
[prop-sf-dualizable-hom] twisted by the invertible local system
$\Lambda(m)_X$, and one computes it locally with a bounded complex
of finite projective modules, where the identification is termwise by
[lem-sf-hom-finite-projective] with compatible differentials and
independent of the chosen resolutions; the coefficient dual and the derived
internal Hom are those of [prop-sf-dualizable] and
[def-weil-derived-pullback-tensor-hom]. The last display is the case
$M=\Lambda_X$ together with the shift of the second variable.
