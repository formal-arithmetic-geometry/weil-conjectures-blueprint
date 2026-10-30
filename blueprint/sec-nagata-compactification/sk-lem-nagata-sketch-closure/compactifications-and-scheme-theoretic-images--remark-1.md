+++
id = "compactifications-and-scheme-theoretic-images--remark-1"
kind = "remark"
title = "Formalization route"
order = 27
uses = ["lemma-nagata-dense-flat-pullback"]
+++
One need not run the affine kernel computations in the proof of
[lemma-nagata-dense-flat-pullback]: one can factor the base-changed
morphism through $\operatorname{SIm}(g)\times_YY'$ and use that
quasi-compact scheme-theoretically dominant morphisms stay
scheme-theoretically dominant under flat base change, which encapsulates
those computations. Only quasi-compactness of $g$ is needed, and
[lemma-nagata-scheme-image-restrict-open] is then the special case of
flat base change along an open immersion, reversing the order of these two
lemmas.
