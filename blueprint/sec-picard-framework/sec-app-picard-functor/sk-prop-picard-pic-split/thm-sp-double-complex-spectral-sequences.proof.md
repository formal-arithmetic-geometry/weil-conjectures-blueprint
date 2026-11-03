+++
kind  = "proof"
of    = "thm-sp-double-complex-spectral-sequences"
+++
By [def-sp-double-complex-total], ${}'F$ and ${}''F$ are decreasing
filtrations of $\operatorname{Tot}(D)$ by subcomplexes with
$F^0\operatorname{Tot}(D)^n=\operatorname{Tot}(D)^n$ and
$F^{n+1}\operatorname{Tot}(D)^n=0$, hence bounded in each degree. So
[thm-sp-spectral-object-yields] applies to each of them: it builds the
bigraded exact couple of the filtration from the long exact cohomology
sequences of $0\to F^{p+1}\to F^p\to\operatorname{gr}^p\to0$, and its
derived couples give a spectral sequence with
$E_1^{p,q}=H^{p+q}(\operatorname{gr}^p\operatorname{Tot}D)$, $d_1$ the
boundary map of $0\to\operatorname{gr}^{p+1}\to F^p/F^{p+2}\to
\operatorname{gr}^p\to0$, and $E_{r+1}\cong\mathcal H(E_r,d_r)$; item (b) of
that theorem gives convergence to $H^\bullet(\operatorname{Tot}D)$ with the
displayed image filtration, which is finite and separated, and item (c)
gives functoriality in the filtered complex, hence in $D$ (a morphism of
double complexes preserves both filtrations).

*The first sequence.* The graded piece $\operatorname{gr}^p_{'F}$ is the
column $D^{p,\bullet}$ placed in total degrees $p+\bullet$, with
differential $(-1)^pd_{II}$; a sign does not change kernels or images, so
${}'E_1^{p,q}=H^{p+q}(\operatorname{gr}^p_{'F})=H^q_{II}(D^{p,\bullet})$.
For $d_1$: a class in ${}'E_1^{p,q}$ is represented by $x\in D^{p,q}$ with
$d_{II}x=0$; viewed in $F^p/F^{p+2}$ its total differential is
$dx=d_Ix+(-1)^pd_{II}x=d_Ix\in D^{p+1,q}=\operatorname{gr}^{p+1}$, so the
boundary map sends $[x]$ to $[d_Ix]$. Hence $d_1$ is the map induced by
$d_I$ on $H^q_{II}$, and ${}'E_2^{p,q}=\mathcal H({}'E_1,d_1)^{p,q}=
H^p_IH^q_{II}(D)$.

*The second sequence.* The graded piece $\operatorname{gr}^q_{''F}$ is the
row $D^{\bullet,q}$ placed in total degrees $\bullet+q$, with differential
$d_I$, so ${}''E_1^{q,p}=H^{p+q}(\operatorname{gr}^q_{''F})=
H^p_I(D^{\bullet,q})$. A class is represented by $y\in D^{p,q}$ with
$d_Iy=0$; in ${}''F^q/{}''F^{q+2}$ one has $dy=(-1)^pd_{II}y\in
D^{p,q+1}=\operatorname{gr}^{q+1}$, so $d_1[y]=(-1)^p[d_{II}y]$. The sign
depends only on $p$, which is constant along the complex
$\bigl(H^p_I(D^{\bullet,q})\bigr)_q$ being formed, so it changes neither
kernels nor images, and ${}''E_2^{q,p}=H^q_{II}H^p_I(D)$.

*Bounds.* In both cases the $E_1$-terms vanish outside the first quadrant
(${}'E_1^{p,q}$ is a subquotient of $D^{p,q}$, ${}''E_1^{q,p}$ one of
$D^{p,q}$), and so do all later pages, which are subquotients of $E_1$. On
page $r$ the differential leaving $(p,q)$ lands in $(p+r,q-r+1)$, outside
the quadrant once $r>q+1$, and the one arriving comes from $(p-r,q+r-1)$,
outside once $r>p$; for $r>\max(p,q+1)$ the page identification
$E_{r+1}\cong\mathcal H(E_r)$ is therefore the identity on the entry
$(p,q)$, which is the stated stabilization. Finally $F^0H^n=H^n$ and
$F^{n+1}H^n=0$ because $F^0\operatorname{Tot}(D)=\operatorname{Tot}(D)$ and
$F^{n+1}\operatorname{Tot}(D)^m=0$ for $m\leq n$, so that
$H^n(F^{n+1}\operatorname{Tot}D)$ is the cohomology of a complex whose
degree-$n$ term vanishes.

(*References: Stacks Project, Homological Algebra, the spectral sequences of
a double complex; Weibel, An Introduction to Homological Algebra, 5.6.*)
