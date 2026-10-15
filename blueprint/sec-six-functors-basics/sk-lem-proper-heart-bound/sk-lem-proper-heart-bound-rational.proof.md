+++
kind = "proof"
of = "det-proper-heart-bound-rational"
+++
By [det-proper-heart-bound-reduction] it suffices to prove the vanishing for $a_!L_0$ and to show that it
passes to $(a_!L_0)[1/\ell]$ and, for $\Qlb$, to the scalar extension. All three are checked on sections
over affine weakly contractible $V\to Y$, using $(R^qp_*N)(V)=H^q(X_V,N|_{X_V})$ from the proof of
[sk-cor-pe-bounded-continuity], and the fact that such $V$ form a basis.

*Lattice.* $H^q(X_V,a_!L_0)=0$ for $q>2d+1$ by [det-proper-heart-bound-lattice].

*Inverting $\ell$.* $(a_!L_0)[1/\ell]=\varinjlim(a_!L_0\xrightarrow{\ell}a_!L_0\xrightarrow{\ell}\cdots)$ is a
filtered colimit, and $H^q(X_V,-)$ commutes with filtered colimits ([sk-cor-pe-bounded-continuity]), so
$H^q(X_V,(a_!L_0)[1/\ell])=\varinjlim H^q(X_V,a_!L_0)=0$ for $q>2d+1$.

*Scalar extension to $\Qlb$.* $\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}N=\varinjlim_{F}F_X\otimes_{E_X}N$ over
finite $F\supset E$, and as a sheaf of abelian groups $F_X\otimes_{E_X}N\cong N^{\oplus[F:E]}$ since $F$ is
finite free over $E$. By continuity again, $H^q(X_V,\overline{\mathbf Q}_{\ell,X}\otimes N)=\varinjlim_FH^q(X_V,N)^{\oplus[F:E]}=0$
for $q>2d+1$, where $N=(a_!L_0)[1/\ell]$.
