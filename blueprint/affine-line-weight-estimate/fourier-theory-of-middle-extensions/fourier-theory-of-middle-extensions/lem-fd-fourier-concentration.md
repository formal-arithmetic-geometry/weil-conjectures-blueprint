+++
id = "lem-fd-fourier-concentration"
kind = "lemma"
title = "Concentration of the transform of a nonexceptional input"
order = 4239
uses = ["def-fd-artin-schreier-sheaf", "def-fd-nonexceptional", "def-wf-fundamental-representation", "lem-a1-affine-hc0", "lem-a1-affine-hc2", "lem-fd-as-lisse"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion with
$U_0=\mathbf A^1_{k_0}\setminus S_0$, put $k=\overline{k}_0$ and
$U=U_0\times_{k_0}k$, let $\mathcal M$ be an irreducible lisse Weil
sheaf on $U_0$ whose geometric fundamental representation
$V=\mathcal M_{\bar\eta}$ (of [def-wf-fundamental-representation])
is irreducible and whose middle extension is
Fourier-nonexceptional in the sense of [def-fd-nonexceptional],
and let $a\in k^\times$. For $\mathcal L_{\psi(ax)}$ the
Artin–Schreier sheaf of [def-fd-artin-schreier-sheaf] on the
$\bar k$-line (lisse of rank one by [lem-fd-as-lisse]), the
nonconstant twisted compact support cohomology is concentrated in
degree one, by the affine-curve computations of
[lem-a1-affine-hc0] and [lem-a1-affine-hc2]:

$$
H^0_c\bigl(\mathbf A^1_k,\,j_!\mathcal M\otimes\mathcal L_{\psi(ax)}\bigr)=0,
\qquad
H^2_c\bigl(\mathbf A^1_k,\,j_!\mathcal M\otimes\mathcal L_{\psi(ax)}\bigr)=0 .
$$

## Proof

The product $\mathcal M\otimes\mathcal L_{\psi(ax)}|_U$ is lisse on the
affine curve $U$ (the tensor of two lisse sheaves), and

$$
j_!\mathcal M\otimes\mathcal L_{\psi(ax)}
=j_!\bigl(\mathcal M\otimes\mathcal L_{\psi(ax)}|_U\bigr):
$$

the Artin–Schreier sheaf is lisse on the line by
[lem-fd-as-lisse], and for a lisse $\mathcal L$ on $\mathbf A^1_k$
the standard exchange $j_!(-)\otimes\mathcal L =j_!(-\otimes j^*\mathcal L)$ holds (both sides have the same stalks in
all degrees, the functor $j_!$ being exact). Hence
$H^q_c(\mathbf A^1_k,j_!\mathcal M\otimes\mathcal L_{\psi(ax)}) =H^q_c(U,\mathcal M\otimes\mathcal L_{\psi(ax)}|_U)$.

For $q=0$ the group vanishes by [lem-a1-affine-hc0], applied to
the lisse Weil sheaf $\mathcal M\otimes\mathcal L_{\psi(ax)}|_U$ on the
smooth geometrically connected affine curve $U$.

For $q=2$, by [lem-a1-affine-hc2] the group is the Tate twist
$(-1)$ of the coinvariants $(V\otimes\chi)_{\pi_1(U)}$, where
$V=\mathcal M_{\bar\eta}$ is the geometric fundamental representation
of [def-wf-fundamental-representation] and $\chi$ is the
geometric representation of $\mathcal L_{\psi(ax)}|_U$: of rank one by
[lem-fd-as-lisse]. The tensor $V\otimes\chi$ of an irreducible
with a rank-one representation is irreducible: if
$W\subseteq V\otimes\chi$ is a nonzero submodule, then
$W\otimes\chi^{-1}$ is a nonzero submodule of $V$, hence all of $V$.
Suppose the coinvariants were nonzero. The coinvariant quotient
$(V\otimes\chi)/I$ with $I=\langle(\gamma-1)w\rangle$ is then nonzero,
so $I$ is a proper $\pi_1(U)$-submodule of the irreducible
$V\otimes\chi$; hence $I=0$, i.e. $\pi_1(U)$ acts trivially, so
$V\otimes\chi$ is a trivial module and $V\cong\chi^{-1}$. Therefore
$\mathcal M\cong\mathcal L_{\psi(-ax)}|_U$: its middle extension is the
Artin–Schreier sheaf of [def-fd-artin-schreier-sheaf] with
parameter $-a$ (the middle extension of the restriction of a lisse
sheaf on the line is the lisse sheaf itself), contradicting the
Fourier-nonexceptionality of [def-fd-nonexceptional] (which in
particular excludes the restriction of $\mathcal L_{\psi(ax')}$ for
every $a'$). This proves $H^2_c=0$.
