+++
kind = "proof"
of = "sk-lem-wft-character-integral"
+++
We first treat the line. From the cohomology of $\mathbf P^1$ and
localization at the point at infinity, we get
$R\Gamma_c(\mathbf A^1,E)=E(-1)[-2]$, identified by the trace map
(Appendix [sec-curve-estimates]). Every translation acts trivially on it,
since it preserves the trace and the cohomology is concentrated in
degree two. Now let $\pi:\mathbf A^1\to\mathbf A^1$, $u\mapsto u^p-u$,
be the Artin–Schreier cover, which is finite étale and whose total
space is again an affine line. Let $\mathcal L_{\psi_0}$ be the
$\psi_0$-eigenspace of $\pi_*E$, that is, the sheaf of the proof of
Lemma [sk-lem-as-properties] for $a=1$. The projector $e_{\psi_0}$ of
that proof cuts out
$R\Gamma_c(\mathbf A^1,\mathcal L_{\psi_0})$ from
$R\Gamma_c(\mathbf A^1,\pi_*E)=R\Gamma_c(\mathbf A^1,E)$ as the
$\psi_0$-eigenspace of the deck translations. These translations act
trivially on the cohomology of the upper line, as we have just seen,
and $\psi_0$ is nontrivial, so this eigenspace is zero. Thus
$R\Gamma_c(\mathbf A^1,\mathcal L_{\psi_0})=0$. By its construction,
$\mathcal L_\psi$ is the pullback of $\mathcal L_{\psi_0}$ by
$x\mapsto ax$, an automorphism of the line, and so
$R\Gamma_c(\mathbf A^1,\mathcal L_\psi)=0$ as well.

For $\lambda\ne0$, we choose linear coordinates in which $\lambda$ is
the first coordinate and apply the Künneth isomorphism of
Lemma [sk-lem-wft-compact-kunneth]. For $\lambda=0$, we apply that
isomorphism $r$ times, and it identifies the top class with the
product of the traces. All these calculations take place with
coefficients in $E$ and commute with extension of scalars.
