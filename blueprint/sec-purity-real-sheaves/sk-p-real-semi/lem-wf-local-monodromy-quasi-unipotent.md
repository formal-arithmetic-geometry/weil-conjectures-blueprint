+++
id = "lem-wf-local-monodromy-quasi-unipotent"
kind = "lemma"
title = "Quasi-unipotence and unipotent normalization of the local monodromy"
order = 2844
uses = ["def-weil-pbc-scheme-conventions", "def-wf-fundamental-representation", "def-wf-weil-group", "lem-wf-local-inertia-finite-parts", "p-real-integral"]
+++
Let $\mathcal F$ be a lisse $\Qlb$-sheaf on a punctured smooth curve
over $k_0$, $\ell\ne\operatorname{char}(k_0)$, and let
$V=\mathcal F_{\bar\eta}$ at a missing point $x$. After a finite
base change ramified only above $x$, the local monodromy of
$\mathcal F$ at $x$ is unipotent: the inertia acts through

$$
\rho(t)=\exp(tN)\qquad(t\in\text{the pro-}\ell\text{-part of the tame inertia}),
$$

with a nilpotent $N:V_\bullet\to V_\bullet(-1)$ satisfying
$F_xNF_x^{-1}=q_x^{-1}N$ for the local Frobenius.

## Proof

By [lem-wf-local-inertia-finite-parts] the images of the wild part
and of the tame factors different from the $\ell$-factor are finite, so
after a finite boundary-ramified base change the inertia acts through
its pro-$\ell$-part
$\mathbf Z_\ell(1)$: this is the classical quasi-unipotence of the
local monodromy of an $\ell$-adic sheaf on a trait for $\ell\ne p$
(Deligne, *La conjecture de Weil II*, (1.8.1), whose
proof for the $\ell$-part is the standard $\ell$-adic-logarithm
statement: the image of the abelian pro-$\ell$ group
$\mathbf Z_\ell(1)$ is contained in $\mathcal O_E$-integral
matrices [p-real-integral], the reduction to the finite residue field is finite, so a
finite-index subgroup lies in the kernel $1+\mathfrak m_E M_n$ of the
reduction, and the $\ell$-adic logarithm identifies that kernel with a
nilpotent-integer Lie algebra: the image is
$\exp(\mathbf Z_\ell\cdot N_{\mathrm{ab}})$-shaped —the recorded
classical input whose elementary ingredients are the finiteness lemma
just cited and the $\ell$-adic Lie computation of the logarithm). The
Frobenius relation $F_xNF_x^{-1}=q_x^{-1}N$ is the conjugation formula
$\sigma t\sigma^{-1}=t^{q_x}$ of the local Weil group
([def-wf-weil-group]) passed through the exponential.
