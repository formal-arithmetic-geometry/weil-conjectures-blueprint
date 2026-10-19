+++
kind  = "proof"
of    = "lem-pc-projective-proper"
uses = ["lemma-nagata-projective-space-base-change-proper"]
+++
An H-projective morphism $f:X\to S$ factors as
$X\xrightarrow{i}\mathbf P^n_S\xrightarrow{\pi}S$ with $i$ a closed
immersion. Closed immersions are proper (Morphisms of Schemes, Lemma
29.42.6, Tag [01W5](https://stacks.math.columbia.edu/tag/01W5)),
$\pi$ is proper ([lemma-nagata-projective-space-base-change-proper]), and
properness is stable under composition. Compositions:
if $g:X\to Y$ and $f:Y\to Z$ are proper, then $f\circ g$ is proper:
it is separated and of finite type (compositions of separated and
finite type morphisms are so), and a universally closed morphism
composed with a universally closed one is universally closed (a base
change of the composite is the composite of the base changes, and
closed maps compose). Therefore $f$ is proper. The last sentence
follows from [lem-pc-proper-base-change] applied along
$\operatorname{Spec}(K)\to\operatorname{Spec}(k)$.
