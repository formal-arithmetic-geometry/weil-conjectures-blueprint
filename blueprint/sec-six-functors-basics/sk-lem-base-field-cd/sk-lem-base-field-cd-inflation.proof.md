+++
kind = "proof"
of = "det-base-field-cd-inflation"
+++
*The periodic resolution.* Let $P(m)$ be the complex of free
$\mathbf Z[C_m]$-modules $P_s=\mathbf Z[C_m]$ ($s\geq0$) with differentials
$P_{2k+1}\to P_{2k}$ multiplication by $\sigma-1$ and $P_{2k+2}\to P_{2k+1}$
multiplication by $N_m$, augmented by the sum of coefficients
$P_0\to\mathbf Z$. It is exact: the image of $\sigma-1$ consists of the elements
with coefficient sum zero, which is the kernel of the augmentation and also the
kernel of $N_m$ (since $N_m\cdot x=(\text{coefficient sum of }x)N_m$); and the
kernel of $\sigma-1$ is the set of elements with all coefficients equal, i.e.
$\mathbf ZN_m$, which is the image of $N_m$. Hence
$H^s(C_m,M)=H^s(\Hom_{C_m}(P(m),M))$, and $\Hom_{C_m}(P_s,M)=M$, with
differentials alternately $\sigma-1$ and $N_m$.

*A chain map over $\pi$.* Define $f_s\colon P(rm)_s\to P(m)_s$ by
$f_s=c_s\,\pi$ with $c_s=r^{\lfloor s/2\rfloor}$, where $\pi$ also denotes the ring
map $\mathbf Z[C_{rm}]\to\mathbf Z[C_m]$. Then $\pi(\sigma'-1)=\sigma-1$ and
$\pi(N_{rm})=rN_m$. Commutation with the odd differentials requires
$c_{2k}=c_{2k+1}$, and with the even ones $c_{2k+2}=rc_{2k+1}$; both hold. In
degree $0$ it is compatible with the augmentations. So $f$ is a
$\pi$-equivariant chain map lifting $\mathrm{id}_{\mathbf Z}$.

*It computes inflation.* Inflation is induced on cochains by any
$\pi$-equivariant chain map between projective resolutions lifting
$\mathrm{id}_{\mathbf Z}$: any two such maps are chain homotopic, by constructing
the homotopy recursively using projectivity of the source terms and exactness of
the target resolution, and the bar resolutions give the cochain description of
inflation. Applying $\Hom(-,M)$ to $f$ gives in degree $s$ the map $M\to M$,
$x\mapsto c_sx$. Hence inflation on $H^s$ is multiplication by
$r^{\lfloor s/2\rfloor}$. If $rM=0$ and $s\geq2$, then $\lfloor s/2\rfloor\geq1$ and
this is zero.
