+++
kind = "proof"
of = "det-pe-sections-conservative"
+++
The objects $\operatorname{Spec}D$ with $D$ w-contractible lie in $\mathcal W$
([det-pe-weak-contractible-equivalences]), and every object $V$ has a covering by them
([det-pe-wcb-cover]). Every $W\in\mathcal W$ has exact sections (the proof of
[det-pe-wc-sections-exact] only uses part 3 of [det-pe-weak-contractible-equivalences]).

*1.* If the sequence is exact, it stays exact on $W$ by exactness of $\Gamma(W,-)$.
Conversely, assume exactness on all $W\in\mathcal W$. Let $b\in B(V)$ with $g(b)=0$. Choose
a covering $\{W_k\to V\}$ with $W_k\in\mathcal W$. Then $b|_{W_k}\in\ker(g(W_k))=
\operatorname{im}(f(W_k))$, so $b$ is locally in the image of $f$, i.e. $b$ is a section of
the image sheaf $\operatorname{im}(f)$ (the sheafification of the presheaf image). Thus
$\ker g\subset\operatorname{im}f$; the reverse inclusion is $g\circ f=0$.

*2.* A complex is acyclic iff it is exact at every term; apply 1 degreewise.

*3.* A morphism $\varphi\colon M\to N$ is an isomorphism iff $0\to M\to N$ and
$M\to N\to0$ are exact; apply 1 (bijectivity on $W$ is exactness of the evaluated
sequences). A morphism of complexes is a quasi-isomorphism iff its cone is acyclic;
evaluation at $W$ commutes with forming cones, so apply 2.
