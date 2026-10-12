+++
kind  = "proof"
of    = "lem-weil-pbc-lisse-generic-kernel"
+++
Let $N=\ker(\phi)$; exactness of the geometric stalk functors gives
$N_{\bar\eta}=0$. Suppose $N\neq0$. By conservativity of geometric stalks,
there is a nonzero geometric germ of $N$, represented by a local section. Use
a common etale refinement on which $F$ is constant. The image of that section
in $F$ can, after another neighbourhood restriction, be taken to be one fixed
nonzero element $m$ of the constant group. We have thus obtained a nonempty
etale $W\to S$ and a section of $N|_W$ whose image is constantly $m\neq0$.

Etale morphisms are flat and locally of finite presentation, so
[lem-weil-pbc-flat-lfp-open] makes the image of $W$ a nonempty open in $S$. It
contains $\eta$, hence $W_{\bar\eta}$ is a nonempty etale scheme over an
algebraically closed field. Choose one of its geometric points. The displayed
section then has nonzero image $m$ in the stalk of $F|_W$, while its stalk in
$N|_W$ is $N_{\bar\eta}=0$, a contradiction. Therefore $N=0$ and $\phi$ is a
monomorphism.
