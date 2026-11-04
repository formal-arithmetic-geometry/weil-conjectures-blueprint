+++
kind = "proof"
of = "det-thm-tf-uniform-formula-weil"
uses = ["sk-thm-tf-uniform-formula", "sk-lem-tf-frobenius-convention", "sk-lem-finite", "sk-thm-sfb-qlbar-two-colimit", "det-prop-sfb-finite-extension-compatibility", "sk-p-trace"]
+++
The automorphism $g_X$ of [def-weil-weil-sheaf-complex] and the semilinear
Frobenius $\operatorname{Fr}_X$ of [sk-def-sf-weil-complexes] are both
induced by the geometric Frobenius of $\operatorname{Gal}(k/k_0)$, so
$(K,\theta)$ is a Weil complex in the sense of [sk-def-sf-weil-complexes],
with $K\in\Dbc(X,\Lambda)=\Dctf(X,\Lambda)$.

(1) By [sk-lem-finite], $\RGammac(X_{\mathrm{pro\acute et}},K)$ is a perfect
complex over the field $\Lambda$, so its cohomology is finite-dimensional and
bounded. The stalk $K_{\bar y}=\bar y^*K$ lies in $\Dctf(\Spec k,\Lambda)$,
which [sk-lem-finite] identifies with $\operatorname{Perf}(\Lambda)$; the
same conclusion follows.

(2) Write $\theta^{[m]}=\theta\circ g_X^*\theta\circ\cdots\circ
(g_X^{m-1})^*\theta$. The compact-support pullback along the automorphism
$g_X$ is natural and compatible with composition, so the operator
$\RGammac(\theta^{[m]})\circ(g_X^m)^\sharp$ of $\theta^{[m]}$ equals
$\RGammac(\theta)\circ g_X^\sharp\circ\RGammac(\theta^{[\,m-1]})\circ
(g_X^{m-1})^\sharp$, and by induction it is the $m$-th power of the operator
of $\theta$, which is $F$. By [sk-lem-tf-frobenius-convention], extended to
$\Lambda$ as in the proof of [sk-thm-tf-uniform-formula], it is the operator
$\operatorname{Frob}_{X,K}^m$ of that theorem, and $F_{y,m}$ is its local
operator $\operatorname{Frob}_{y,m}$. The boxed identity is therefore the
identity (2) of [sk-thm-tf-uniform-formula]. Over the field $\Lambda$ the
categorical trace of an endomorphism of a perfect complex is the alternating
sum of the traces on cohomology ([sk-p-trace]), so both sides are also the
categorical traces of (1) of [sk-thm-tf-uniform-formula].

(3) Extension of scalars $\Qlb_X\otimes_{E'_X}-$ is exact, because
$\Qlb_X$ is flat over $E'_X$, and it commutes with $g_X^*$, with
$\RGammac$ and with stalks ([det-prop-sfb-finite-extension-compatibility]).
It carries the operators of $\theta'$ to those of $\theta$. Hence
$\RGammac(X,K)\simeq\RGammac(X,K')\otimes_{E'}\Qlb$ and
$K_{\bar y}\simeq K'_{\bar y}\otimes_{E'}\Qlb$ with the extended operators;
since $\Qlb$ is flat over $E'$, the same holds on cohomology. The trace of
the scalar extension of an $E'$-linear endomorphism of a finite-dimensional
space is the image of its trace. Both sides of (2) are defined from
$(K,\theta)$ alone, so the identity does not depend on the model. Two models
become isomorphic as Weil complexes over a common finite extension
([sk-thm-sfb-qlbar-two-colimit] (1)), and their operators are then
conjugate, which gives the same $E'$-valued traces.
