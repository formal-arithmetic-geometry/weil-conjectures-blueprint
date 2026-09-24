+++
id = "lem-wf-unipotent-invariants-kernel"
kind = "lemma"
title = "Inertia invariants of a unipotent local monodromy"
order = 4205
uses = ["def-weil-pbc-scheme-conventions", "def-wf-fundamental-representation", "def-wf-middle-extension", "def-wf-weil-group", "lem-wf-boundary-stalk-invariants", "lem-wf-local-monodromy-quasi-unipotent"]
+++
Let $\mathcal F$ be a lisse $\Qlb$-sheaf on a punctured smooth curve
over $k_0$, $\ell\ne\operatorname{char}(k_0)$, let $x$ be a missing
point, and let $V=\mathcal F_{\bar\eta}$ be the local geometric generic
stalk at $x$, with inertia group $I_x$ acting through the
fundamental representation
of [def-wf-fundamental-representation]. Assume that after a finite
base change ramified only above $x$ the local monodromy of
$\mathcal F$ at $x$ is unipotent in the normal form of
[lem-wf-local-monodromy-quasi-unipotent]: the inertia acts through

$$
\rho(t)=\exp(tN)\qquad(t\in\text{the pro-}\ell\text{-part of the tame inertia}),
$$

with a nilpotent $N:V_\bullet\to V_\bullet(-1)$ satisfying
$F_xNF_x^{-1}=q_x^{-1}N$ for the local Frobenius. Then the
unipotent-normalized inertia group of any element of the
pro-$\ell$-part has the same kernel for $N$ and for the inertia
invariants, and the boundary stalk of the middle extension
$\mathcal F\mapsto j_*\mathcal F$ of [def-wf-middle-extension] at
$x$ is that common kernel:

$$
(j_*\mathcal F)_{\bar x}=V^{I_x}=\ker N .
$$

## Proof

By [lem-wf-local-monodromy-quasi-unipotent] the local monodromy at
$x$ is unipotent after the finite boundary-ramified base change, so on
the pro-$\ell$-part of the tame inertia it is of the displayed form
$\rho(t)=\exp(tN)$ with $N$ nilpotent. For $t\neq0$ in that
pro-$\ell$-part one has $\exp(tN)-I=tN\,h(tN)$ with $h$ the
invertible power series $h(x)=(e^x-1)/x$, so
$\exp(tN)v=v$ if and only if $Nv=0$: the invariants of the unipotent
action are exactly the kernel of $N$, and the indices are kept under
the base change. By the boundary-stalk description of
[lem-wf-boundary-stalk-invariants] the boundary stalk of the middle
extension of [def-wf-middle-extension] at $x$ is the space
$V^{I_x}$ of inertia invariants, whence
$(j_*\mathcal F)_{\bar x}=V^{I_x}=\ker N$.
