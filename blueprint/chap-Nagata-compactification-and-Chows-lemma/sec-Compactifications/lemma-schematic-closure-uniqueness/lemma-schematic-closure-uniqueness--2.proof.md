+++
kind = "proof"
of = "lemma-schematic-closure-uniqueness--2"
uses = ["lemma-schematic-closure-uniqueness--1"]
+++
Write $X\xrightarrow{j}Z\xrightarrow{k}T$ for the factorization
through the scheme-theoretic image. Factor the base-changed
morphism through $Z\times_TT'$. Its first factor is the flat
base change of $j$. The morphism $j$ is quasi-compact because $f$
is quasi-compact and $k$ is a closed immersion, and it is
scheme-theoretically dominant by [lemma-schematic-closure-uniqueness--1].
Its base change is therefore scheme-theoretically dominant, by
`AlgebraicGeometry.IsSchemeTheoreticallyDominant.of_isPullback`.

Composing a morphism with a scheme-theoretically dominant first
factor leaves its kernel ideal unchanged. Hence the kernel of the
base-changed morphism is the kernel of the closed immersion
$Z\times_TT'\to T'$, namely $\mathcal I_f\mathcal O_{T'}$.
This proves `AlgebraicGeometry.Scheme.Hom.ker_pullback_snd` for
the chosen fibre product. Transport along the canonical isomorphism
from any cartesian square to this fibre product gives the stated
formula. Open immersions are flat, giving the final assertion.
