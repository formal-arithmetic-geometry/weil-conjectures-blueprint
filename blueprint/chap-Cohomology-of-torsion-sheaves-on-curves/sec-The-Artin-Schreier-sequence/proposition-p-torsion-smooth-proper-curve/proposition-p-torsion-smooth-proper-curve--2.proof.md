+++
kind = "proof"
of = "proposition-p-torsion-smooth-proper-curve--2"
order = 1584006
uses = ["lemma-coherent-base-change-invertible-sheaves"]
+++
Use the Artin–Schreier sequences on $C$ and $C'$, with additive sheaves
$G$ and $G'$ and maps $\wp$ and $\wp'$ given by $a\mapsto a^p-a$.
The pullback of functions gives a map $\iota^*G\to G'$ compatible with
the two sequences. Proper connectedness and smoothness identify the
global functions on each curve with its ground field, where
$a\mapsto a^p-a$ is surjective.

The étale/Zariski comparison and coherent base change
[lemma-coherent-base-change-invertible-sheaves] supply a
finite-dimensional scalar model $V$ for $H^1(C,G)$ and a model
$k'\otimes_k V$ for $H^1(C',G')$. Multiplication on sections induces
the scalar actions. Applying cohomology to $\wp+1$ gives $\varphi$;
the identity $(ca)^p=c^pa^p$ proves its Frobenius-linearity. The same
construction gives $\varphi'$. Naturality of powers and of the scalar
comparison gives $\varphi'(1\otimes v)=1\otimes\varphi(v)$. These
are the compatible rows of
`AlgebraicGeometry.IsCurve.exists_artinSchreier_frobenius_exact_rows`.

In each long exact sequence, surjectivity in degree zero makes the
map from $H^1$ of the constant sheaf injective. Its image is the
kernel of $H^1(\wp)$, which becomes $\ker(\varphi-1)$ under the scalar
model. This constructs $e$ and $e'$. The square of exact sequences
and the identity for coherent pullback give
$e'(\iota^*x)=1\otimes e(x)$. For dimension zero, the scalar model is
zero and the same argument applies.
