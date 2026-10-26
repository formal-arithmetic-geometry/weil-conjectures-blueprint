+++
kind = "proof"
of = "sk-prop-sp-integral-towers"
uses = ["sk-lem-int-integral-heart", "sk-prop-integral-criterion", "sk-lem-int-tensor"]
+++
For (1), by [sk-lem-int-integral-heart], $K$ is a finite extension of shifted sheaves $a_!C$
with $C$ of Tor amplitude $[-1,0]$ on a stratum. Tor amplitude and constructibility of the
reductions are preserved by extensions and shifts, and the number of steps and the shifts do
not depend on $n$, which gives the bounds independent of $n$. For (2), the reduction
$K/\pi_E=(K/\ell)\otimes^{\mathbf L}_{\mathcal O_E/\ell}\mathcal O_E/\pi_E$ is bounded
constructible, and so $K\in\Dbc(T,\mathcal O_E)$ by the criterion (2)$\Rightarrow$(1) of
[sk-prop-integral-criterion]. Part (3) is [sk-lem-int-tensor].
