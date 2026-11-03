+++
kind  = "proof"
of    = "lem-sc-constant-locus-closed"
+++
Consider the morphism

$$
\Phi=(f\circ\operatorname{pr}_{13},\,f\circ\operatorname{pr}_{23}):
X\times_kX\times_kY\longrightarrow Z\times_kZ,\qquad
\Phi(x_1,x_2,y)=(f(x_1,y),f(x_2,y)),
$$

the projection $\pi:X\times_kX\times_kY\to Y$, and the diagonal
$\Delta_Z\subseteq Z\times_kZ$. Since $Z$ is separated over $k$,
$\Delta_Z$ is closed, so $U:=\Phi^{-1}(Z\times_kZ\smallsetminus\Delta_Z)$
is open in $X\times_kX\times_kY$. If $X=\emptyset$ then every
$f_{\bar y}(X_{\overline{\kappa(y)}})$ is empty, so $L=Y$ is closed;
assume from now on $X\ne\emptyset$.

*Claim: $y\in L$ if and only if $\pi^{-1}(y)\subseteq\Phi^{-1}(\Delta_Z)$,
i.e. $L=Y\smallsetminus\pi(U)$.* Put $K=\overline{\kappa(y)}$. The base
change of $\pi$ along $\bar y$ is $X_K\times_KX_K$, and the map
$X_K\times_KX_K\to\pi^{-1}(y)$ is surjective (base change of the
surjection $\Spec K\to\Spec\kappa(y)$). On $X_K\times_KX_K$ the morphism
$\Phi$ factors as
$f_{\bar y}\times f_{\bar y}:X_K\times_KX_K\to Z_K\times_KZ_K$ followed
by the projection $Z_K\times_KZ_K=(Z\times_kZ)_K\to Z\times_kZ$, under
which the preimage of $\Delta_Z$ is $\Delta_{Z_K}$. Hence
$\pi^{-1}(y)\subseteq\Phi^{-1}(\Delta_Z)$ iff
$f_{\bar y}\times f_{\bar y}$ maps $X_K\times_KX_K$ into $\Delta_{Z_K}$.

If $f_{\bar y}(X_K)=\{z\}$, then $z$ is the image of a $K$-point of
$X_K$ (which is of finite type over the algebraically closed $K$), so
$z$ is a $K$-point, and the only point of $Z_K\times_KZ_K$ lying over
$(z,z)$ is the point of $\Spec(K\otimes_KK)$, which is on
$\Delta_{Z_K}$. Conversely, suppose $f_{\bar y}\times f_{\bar y}$ maps
into $\Delta_{Z_K}$. For $K$-points $x_1,x_2$ of $X_K$, the $K$-point
$(x_1,x_2)$ maps to the $K$-point $(f_{\bar y}(x_1),f_{\bar y}(x_2))$,
which lies on $\Delta_{Z_K}$ only if $f_{\bar y}(x_1)=f_{\bar y}(x_2)$.
For an arbitrary point $x\in X_K$, the closed subset
$\overline{\{x\}}$ contains a closed point $x'$, a $K$-point; choose a
point of $X_K\times_KX_K$ with projections $x$ and $x'$ (the fibre
product of $\Spec\kappa(x)$ and $\Spec\kappa(x')$ over $K$ is
nonempty); its image lies on $\Delta_{Z_K}$, so
$f_{\bar y}(x)=f_{\bar y}(x')$. Thus $f_{\bar y}(X_K)$ is a single
point (it is nonempty, as $X_K\ne\emptyset$). This proves the claim.

Finally $\pi$ is the base change of $X\times_kX\to\Spec k$ along
$Y\to\Spec k$; it is flat and locally of finite presentation ($X$ is of
finite type over the field $k$), hence open (Stacks Project, Morphisms,
Lemma 29.26.10, [Tag 01UA](https://stacks.math.columbia.edu/tag/01UA)).
So $\pi(U)$ is open and $L=Y\smallsetminus\pi(U)$ is closed in $Y$.
