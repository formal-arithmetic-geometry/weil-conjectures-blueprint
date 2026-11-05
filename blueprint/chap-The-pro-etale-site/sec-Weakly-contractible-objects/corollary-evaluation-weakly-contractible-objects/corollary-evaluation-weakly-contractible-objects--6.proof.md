+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects--6"
order = 79012
uses = ["definition-weak-contractibility", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects"]
+++
Put $Z=\ker g$ and let $a\colon A\to Z$ be induced by $f$. Exactness
at $B$ is equivalent to $a$ being an epimorphism. The forgetful functor
to abelian sheaves preserves finite colimits and reflects
epimorphisms, so this is equivalent to local surjectivity of the
underlying abelian map. Kernels are sectionwise, and exactness after
evaluation at $W$ is equivalent to surjectivity of $a(W)$.

If $a$ is locally surjective, weak contractibility makes $a(W)$
surjective. Conversely, cover any site object by spectra of
w-contractible rings using
[theorem-enough-affine-weakly-contractible-objects]. These are affine
and weakly contractible by [lemma-w-contractible-affines-projective].
Surjectivity on these objects supplies local lifts of every section of
$Z$, proving local surjectivity and hence exactness.

Apply the short-sequence criterion to the adjacent differentials in
every degree of $K$. Exchanging the quantifiers over the degree and
$W$ proves the acyclicity criterion, without a boundedness hypothesis.
