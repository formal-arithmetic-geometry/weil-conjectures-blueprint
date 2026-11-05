+++
kind = "proof"
of = "proposition-base-change-fourier-inversion--3"
order = 1229004
uses = ["proposition-composition-base-change-rf-shriek", "lemma-artin-schreier-character-sheaf", "proposition-topos-functoriality", "prose-10-20"]
+++
Let $\iota_a:A\to A\times A^\vee$ be $x\mapsto(x,a)$.
The square formed by $\iota_a,p,p_2,i_a$ is cartesian, so compact-support
base change [proposition-composition-base-change-rf-shriek] gives
$i_a^*Rp_{2!}\simeq Rp_!\iota_a^*$, compatibly with the Weil
structures [prose-10-20]. Pullback commutes with tensoring by the lisse
kernel, and $p_1\iota_a=\operatorname{id}_A$. The restriction of
$\mathcal K_\psi$ along $\iota_a$ is $\mathcal L_{\psi(ax)}$, since
the pairing $x\xi$ restricts to $ax$. Moving the shift $[1]$ through
pullback and composing these isomorphisms proves the functorial formula.

For the cohomology formula, the point $a$ and the unique point of
$\operatorname{Spec}k_0$ both have degree one over $k_0$. Pullback
therefore identifies their stalks with the same Frobenius, and the
stalk on $\operatorname{Spec}k_0$ identifies with geometric global
sections. Cohomology sheaves commute with pullback; applying this to the
functorial formula and using
$\mathcal H^n(C[1])\simeq\mathcal H^{n+1}(C)$ gives the asserted
Frobenius-equivariant isomorphism.
