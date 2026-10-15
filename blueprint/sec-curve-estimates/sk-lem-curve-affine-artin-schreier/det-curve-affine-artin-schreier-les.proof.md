+++
kind = "proof"
of = "det-curve-affine-artin-schreier-les"
+++
The sequence

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{\ \wp\ }\mathbf G_a\longrightarrow0
$$

is exact on $U_{\mathrm{ét}}$. The kernel of $\wp$ is $\mathbf F_p$ because
$y^p-y=\prod_{c\in\mathbf F_p}(y-c)$: for $y\in\cO(V)$ with $y^p=y$ the
elements $y-c$ are pairwise comaximal (their differences are units of
$\mathbf F_p$), so by the Chinese remainder theorem $V$ is the disjoint union
of the closed and open pieces $\{y=c\}$, i.e. $y$ is a locally constant
$\mathbf F_p$-valued function. Surjectivity holds étale
locally: for $f\in\cO(V)$ the $\cO(V)$-algebra $\cO(V)[y]/(y^p-y-f)$ is free
of rank $p$ and étale because the derivative of $y^p-y-f$ is $-1$, and $y$ is
a $\wp$-preimage of $f$ on it (this is [lem-sc-as-sequence] when $U$ is a
curve; the argument is the same for any scheme over $\mathbf F_p$).

Here $\mathbf G_a$ is the étale sheaf $\cO_{\mathrm{ét}}$ associated with the
quasi-coherent module $\cO_U$ ([def-sc-etale-qcoherent-module]). Since $U$ is
affine, $H^q(U_{\mathrm{ét}},\mathbf G_a)=0$ for $q>0$
([lem-sc-etale-affine-qcoherent]), and $H^0(U_{\mathrm{ét}},\mathbf G_a)=A$.
The long exact cohomology sequence therefore reads

$$
0\to H^0(U,\mathbf F_p)\to A\xrightarrow{\wp}A\xrightarrow{\delta}
H^1(U,\mathbf F_p)\to H^1(U,\mathbf G_a)=0,
$$

and $0=H^{q-1}(U,\mathbf G_a)\to H^q(U,\mathbf F_p)\to H^q(U,\mathbf G_a)=0$
for $q\geq2$. Hence $\delta$ induces $A/\wp(A)\xrightarrow{\sim}H^1(U,\mathbf F_p)$
and the higher groups vanish. By the construction of the boundary map,
$\delta(a)$ is the class of the torsor of local $\wp$-preimages of $a$, i.e.
of local solutions of $y^p-y=a$. A morphism of affine $\mathbf F_p$-schemes
pulls back the Artin–Schreier sequence to the Artin–Schreier sequence, so the
long exact sequences and hence the identifications are natural.
