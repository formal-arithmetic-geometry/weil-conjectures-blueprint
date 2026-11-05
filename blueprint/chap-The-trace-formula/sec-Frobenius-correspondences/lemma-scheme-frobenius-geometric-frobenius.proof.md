+++
kind = "proof"
of = "lemma-scheme-frobenius-geometric-frobenius"
order = 954
uses = ["definition-frobenius-operator", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "lemma-scheme-frobenius-geometric-frobenius--2", "lemma-scheme-frobenius-geometric-frobenius--3"]
+++
The maps $\Phi_X$ and $\operatorname{Fr}_X$ differ by the
absolute Frobenius, and pullback along the absolute Frobenius is
naturally the identity on étale sheaves. This gives $\kappa_m$, and a compatibility between the two identifications of compact cohomology, checked on a compactification descended from $X_0$, shows that $\kappa_m$ carries one pullback map on cohomology to the other.
On coordinate rings the two maps are

$$
\Phi_X^\#(a\otimes b)=a^q\otimes b,
\qquad \operatorname{Fr}_X^\#(a\otimes b)=a\otimes b^{1/q}
$$

so that $\Phi_X=F_X\operatorname{Fr}_X$, where
$F_X$ is the absolute $q$-power Frobenius of $X$. Now, on the classical constructible category, pullback along absolute Frobenius is
naturally isomorphic to the identity, because for an étale object
its relative Frobenius is an isomorphism, functorial in that object.
Transporting this natural isomorphism to $D^b_{\mathrm{ctf}}(X,A)$ by the
comparison with the pro-étale site, we obtain $\kappa_m$ together with its compatibility with
iteration, and the latter gives $\psi_m=\phi_m\kappa_m$.

For the pullback maps $(\Phi_X^m)^*$ and $(\operatorname{Fr}_X^m)^*$ on compact cohomology, put $C=R\Gamma_c(X,-)$, let $\beta:R\Phi_{X*}\xrightarrow{\sim}R\operatorname{Fr}_{X*}$ be the mate of $\kappa_1$, and let $\iota_\Phi:CR\Phi_{X*}\xrightarrow{\sim}C$ and $\iota_{\operatorname{Fr}}:CR\operatorname{Fr}_{X*}\xrightarrow{\sim}C$ be the identifications of compact cohomology entering the two pullback maps, the second one including $\lambda_\gamma$ of Definition [definition-frobenius-operator]. What is needed is the equation

$$
\iota_{\operatorname{Fr}}\circ C(\beta)=\iota_\Phi.
$$

A generic mate identity does not give it with these fixed identifications; it has to be checked with the normalized trivialization of pullback along absolute Frobenius that defines $\kappa_1$. We check it over a compactification of $X$ descended from $X_0$: extend $\Phi_X$ and $\operatorname{Fr}_X$ to the compactification, compare the trivialization with proper direct image and with $j_!$, and read off the equation from the resulting diagram. Unit compatibility then gives $C(\kappa_1)\circ\Phi_X^*=\operatorname{Fr}_X^*$ as maps $R\Gamma_c(X,K)\to R\Gamma_c(X,\operatorname{Fr}_X^*K)$. The case of $m$ follows by iteration, using the formula $\eta_{L_2L_1}=(R_1\eta_2L_1)\circ\eta_1$ for the unit of a composite adjunction together with the coherence of the composition isomorphisms and of $\lambda_\gamma$. Composing with $\phi_m$, or with an arbitrary morphism $(\operatorname{Fr}_X^m)^*K\to K$, we obtain the equality of operators.
