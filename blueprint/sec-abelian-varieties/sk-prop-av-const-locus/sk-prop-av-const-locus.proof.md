+++
kind  = "proof"
of    = "sk-prop-av-const-locus"
+++
Let $\Phi=(f\circ\mathrm{pr}_{13},f\circ\mathrm{pr}_{23}):
X\times_kX\times_kY\to Z\times_kZ$, i.e.
$\Phi(x_1,x_2,y)=(f(x_1,y),f(x_2,y))$, and let
$\pi:X\times_kX\times_kY\to Y$ be the projection. Since $Z$ is
separated, $\Delta_Z$ is closed, so $U:=\Phi^{-1}(Z\times_kZ\smallsetminus
\Delta_Z)$ is open. We claim $y\in L$ iff
$\pi^{-1}(y)\subseteq\Phi^{-1}(\Delta_Z)$, i.e. $L=Y\smallsetminus\pi(U)$.
Put $K=\overline{\kappa(y)}$; then $X_K\times_KX_K\to\pi^{-1}(y)$ is
surjective, and on it $\Phi$ factors through
$f_{\bar y}\times f_{\bar y}:X_K\times_KX_K\to Z_K\times_KZ_K$, where
the preimage of $\Delta_Z$ is $\Delta_{Z_K}$. If $f_{\bar y}(X_K)$ is
empty there is nothing to show; if $f_{\bar y}(X_K)=\{z\}$,
then $z$ is a $K$-point and the only point of $Z_K\times_KZ_K$ over
$(z,z)$ lies on $\Delta_{Z_K}$. Conversely, if
$f_{\bar y}\times f_{\bar y}$ maps into $\Delta_{Z_K}$, then
$f_{\bar y}(x_1)=f_{\bar y}(x_2)$ for $K$-points $x_1,x_2$; for an
arbitrary $x\in X_K$ pick a $K$-point $x'\in\overline{\{x\}}$ ($X_K$ is
of finite type over $K=\bar K$) and a point of $X_K\times_KX_K$ over
$(x,x')$ to get $f_{\bar y}(x)=f_{\bar y}(x')$; so $f_{\bar y}(X_K)$ consists of
at most one point (if $X=\emptyset$, both sides of the claim hold
trivially). Finally $\pi$ is the
base change of $X\times_kX\to\Spec k$, hence flat and locally of
finite presentation, hence open (`01UA`); so $\pi(U)$ is open
and $L$ is closed.
