+++
kind = "proof"
of = "sk-lem-tf-rational-model"
uses = ["sk-thm-sfb-rationalization-comparison", "sk-lem-integral-models"]
+++
The rationalization comparison of the section on derived functors of
module sheaves ([sk-thm-sfb-rationalization-comparison]), together with the
localized Hom comparison of the section on smooth purity,

$$
 \Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E
 \xrightarrow{\ \sim\ }
 \Hom_{\Dbc(X,E)}\bigl(K_0[1/\ell],L_0[1/\ell][q]\bigr),
 \tag{2}
$$

gives

$$
 \Dbc(X,\mathcal O_E)[1/\ell]\simeq\Dbc(X,E).
$$

For objects this works as follows. [sk-lem-integral-models] (4)
provides integral models for a set of generators under finite cones.
If two objects have integral models, a morphism between them lifts
after multiplication by a power of $\pi_E$, by the localized Hom
comparison (2), and the integral cone of that lift rationalizes to the
given cone because $\pi_E$ is invertible over $E$. Induction over finite
cones and shifts gives an integral model $K_0$ of $K_E$, also when a
lisse sheaf has no global lisse lattice.

Inverse image preserves integral constructibility, so
$\Phi_X^*K_0$ is an integral model of $\Phi_X^*K_E$. Applying the
localized Hom comparison (2) to the pair $(\Phi_X^*K_0,K_0)$ writes
$\psi_E$ as $\pi_E^{-N}\theta$. Since pullback is $\mathcal O_E$-linear,
the $m$-th iterate is $(\psi_E)_m=\pi_E^{-Nm}(\theta_m\dt E)$.
Coefficient comparison for compact cohomology and for stalks
identifies the compact-support pullbacks as well, and gives
(1).

In the language of lattices and reduction towers this is
[prop-trf-rational-frobenius-integral-model].
