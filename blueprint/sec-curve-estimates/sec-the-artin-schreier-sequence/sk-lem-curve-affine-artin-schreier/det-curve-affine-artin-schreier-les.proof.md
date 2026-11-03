+++
kind = "proof"
of = "det-curve-affine-artin-schreier-les"
+++
The sequence

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{\ \wp\ }\mathbf G_a\longrightarrow0
$$

is exact on $U_{\mathrm{ét}}$ ([lem-sc-as-sequence]).

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
and the higher groups vanish.
