+++
kind  = "proof"
of    = "sk-thm-picard-rr"
+++
This is coherent duality and Riemann–Roch for smooth curves (Stacks
Project, Tag 0B5B); the duality is given by the residue trace on
differentials ([det-thm-picard-duality], with $n=1$, $q=1$, $\cF=\cL$).

*Riemann–Roch.* By additivity of $\chi$ in short exact sequences, the
torsion part of a coherent $\cF$ (for which $\chi=h^0$ is the length,
i.e. the degree) and a filtration of the locally free quotient by line
bundles (along which $\deg\det$ is additive) reduce the formula to line
bundles $\cO_C(D)$. There
$0\to\cO_C(D-x)\to\cO_C(D)\to\kappa(x)\to0$ gives
$\chi(\cO_C(D))=\chi(\cO_C(D-x))+[\kappa(x):k]$ (coherent cohomology
vanishes in degrees $\ge2$ on the one-dimensional noetherian space $C$,
so $\chi=h^0-h^1$ throughout); applied to $D$ when $n_x>0$ and to $D+x$
when $n_x<0$, it lowers $\sum_x|n_x|$ by one and leaves $\chi-\deg$
unchanged, so by induction $\chi(\cO_C(D))=\deg D+\chi(\cO_C)$, and
$\chi(\cO_C)=h^0-h^1=1-g$ because $H^0(C,\cO_C)=k$. (In particular
$C$ is connected, and, its local rings being regular, integral.)

*Canonical degree and genus.* Duality with $\cL=\cO_C$ gives $h^0(\omega_{C/k})=g$
and $h^1(\omega_{C/k})=h^0(\cO_C)=1$, so
$\deg\omega_{C/k}=\chi(\omega_{C/k})-\chi(\cO_C)=(g-1)-(1-g)=2g-2$.

*Field extension.* For $K/k$, flat base change identifies
$H^i(C_K,\cL_K)=H^i(C,\cL)\otimes_kK$ for all $i$, so
$\chi(C_K,\cL_K)=\chi(C,\cL)$; applied to $\cL$ and to $\cO_C$ this shows
that the degree $\chi(\cL)-\chi(\cO_C)$ and the genus $h^1(\cO_C)$ are
preserved, and that $H^0(C_K,\cO_{C_K})=K$, so $C_K$ again satisfies the
hypotheses. The degree and $\chi$ are invariant under field extension
by flat base change for coherent cohomology.

*Vanishing.* If $\deg\cL>2g-2$, the dual sheaf
$\omega_{C/k}\otimes\cL^{-1}$ has negative degree. A nonzero section of
an invertible sheaf on an integral curve has an effective zero divisor,
of degree $\ge0$, so a negative-degree sheaf has no nonzero section.
Hence $H^1(C,\cL)=0$, and Riemann–Roch gives
$h^0(C,\cL)=\chi(C,\cL)=\deg\cL+1-g$.

*(G).* Ampleness descends along $\Spec\bar k\to\Spec k$ and degree is
preserved by flat base change, so we may take $k$ algebraically closed,
where every closed point is rational. For $m\deg\cL\ge2g+1$ and closed
points $P,Q$ (possibly equal), the range $\deg>2g-2$ above gives
$h^0(\cL^{\otimes m}(-P))=h^0(\cL^{\otimes m})-1$ and
$h^0(\cL^{\otimes m}(-P-Q))=h^0(\cL^{\otimes m})-2$, i.e.
$\cL^{\otimes m}$ is base-point free and separates points and tangent
vectors; hence $\cL^{\otimes m}$ is very ample and $\cL$ is ample.

*(H).* Classical: the complement of the support of an ample effective
Cartier divisor $D$ is the non-vanishing locus of the canonical section
of $\cO_X(D)$, and non-vanishing loci of sections of an ample sheaf on a
proper scheme are affine.
