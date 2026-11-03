+++
kind = "proof"
of = "det-sp-zero-section-cartier"
uses = ["thm-nagata-blowup-principalizes-center", "thm-nagata-global-blowup-proper", "thm-nagata-global-blowup-complement", "thm-weil-pbc-bounded-below", "det-sp-defect-proper-smooth"]
+++
The pullback ideal $I\mathcal O_{X'}$ is invertible on the blow-up
[thm-nagata-blowup-principalizes-center], so $Z'$ is an effective Cartier divisor (empty components
cause no problem), and $b$ is proper [thm-nagata-global-blowup-proper].

The unit $L\to Rb_*b^*L$ is an isomorphism. Away from $Z$ this holds because $b$ is an isomorphism
there [thm-nagata-global-blowup-complement]. On $Z$, proper base change
[thm-weil-pbc-bounded-below] identifies the stalks of the target with the cohomology of the fibres
of $b$ with coefficients $b^*L$ restricted to the fibre, which are zero because $i^*L=0$; the
source vanishes there as well.

The proper case of [det-sp-defect-proper-smooth] for $b$ then gives

$$
C_{X,Z}(L)\simeq C_{X,Z}(Rb_*b^*L)\simeq Rb_{Z*}C_{X',Z'}(b^*L).
$$
