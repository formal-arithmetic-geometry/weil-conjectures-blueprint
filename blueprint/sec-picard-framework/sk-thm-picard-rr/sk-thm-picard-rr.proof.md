+++
kind  = "proof"
of    = "sk-thm-picard-rr"
uses = ["sk-thm-picard-duality"]
+++
(RR): by additivity of $\chi$ in short exact sequences, the torsion
part of $\cF$ (for which $\chi=h^0$ is the length, i.e. the degree) and a
filtration of the locally free quotient by line bundles (along which
$\deg\det$ is additive) reduce the formula to
line bundles $\cO_X(D)$. There $0\to\cO_X(D-x)\to\cO_X(D)\to\kappa(x)\to0$
gives $\chi(\cO_X(D))=\chi(\cO_X(D-x))+[\kappa(x):k]$ (coherent
cohomology vanishes in degrees $\ge2$ on the one-dimensional noetherian
space $X$, so $\chi=h^0-h^1$ throughout); applied to $D$ when $n_x>0$
and to $D+x$ when $n_x<0$ (where it reads
$\chi(\cO_X(D))=\chi(\cO_X(D+x))-[\kappa(x):k]$), it lowers
$\sum_x|n_x|$ by one and leaves $\chi-\deg$ unchanged, so by induction on
$\sum_x|n_x|$, $\chi(\cO_X(D))=\deg D+\chi(\cO_X)$, and
$\chi(\cO_X)=h^0-h^1=1-g$ by the hypotheses; this is also the equality
$\deg\cL=\chi(\cL)-\chi(\cO_X)$. For $d\ge2g-1$,
[sk-thm-picard-duality] gives
$H^1(\cL)^\vee\cong H^0(\omega_X\otimes\cL^{-1})=0$, the latter of
negative degree ($\deg\omega_X=\chi(\omega_X)-\chi(\cO_X)=2g-2$, as
duality gives $h^0(\omega_X)=g$, $h^1(\omega_X)=1$; a nonzero section
would give an effective divisor of negative degree), whence $h^0(\cL)=d+1-g$. (G): ampleness descends along the
fpqc cover $\Spec\bar k\to\Spec k$ and $\deg$ is preserved by flat
base change, and $X_{\bar k}$ is again a smooth proper connected curve
of genus $g$ with $H^0=\bar k$ ($X$ is geometrically reduced with
$H^0(X,\cO_X)=k$, hence geometrically integral); so we may take $k$
algebraically closed, where every closed point is rational. Then for
$m\deg\cL\ge2g+1$ and closed points $P,Q$ (possibly equal), (RR) in
the range $d\ge2g-1$ gives
$h^0(\cL^{\otimes m}(-P))=h^0(\cL^{\otimes m})-1$ and
$h^0(\cL^{\otimes m}(-P-Q))=h^0(\cL^{\otimes m})-2$, i.e.
$\cL^{\otimes m}$ is base-point free and separates points and tangent
vectors; hence $\cL^{\otimes m}$ is very ample and $\cL$ is ample.
(H): classical (the complement of an
ample effective divisor is affine).
