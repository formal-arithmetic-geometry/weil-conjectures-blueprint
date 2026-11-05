+++
kind = "proof"
of = "proposition-fourier-transform-middle-extension--1"
order = 1264002
uses = ["proposition-fourier-inversion", "proposition-composition-base-change-rf-shriek", "proposition-projection-formula-rational-coefficients", "lemma-finite-quasi-finite-direct-images", "lemma-artin-schreier-character-sheaf"]
+++
Choose a finite reduced closed subscheme $i:Z_0\hookrightarrow
\mathbf A^{1\vee}_{k_0}$ containing the support of $G$. On
$Z_0\times_{k_0}\mathbf A^1_{k_0}$, write $q$ for the projection to
$Z_0$, $\pi$ for the projection to the line, and $i'$ for the map into
the product of the two lines. Since $G\simeq i_*i^*G$, base change,
the projection formula, and the composition law give

$$
\operatorname{FT}_{\psi^{-1}}(G)
\simeq H[1],\qquad
H=\pi_*\bigl(i'^*\mathcal K_{\psi^{-1}}\otimes q^*i^*G\bigr).
$$

Here $\pi$ is finite, so its direct image on sheaves is exact by
[lemma-finite-quasi-finite-direct-images]. Fourier inversion
[proposition-fourier-inversion] now gives

$$
(j_*M)[1](-1)\simeq H[1].
$$

Taking cohomology in degree $-1$ and forgetting the Weil structure
identifies the geometric sheaves underlying $j_*M$ and $H$, since the
Tate twist is geometrically constant.

Over $\bar k_0$, the scheme $Z_0$ is a finite disjoint union of points.
On the line over a point with coordinate $b$, the kernel restricts to
$\mathcal L_{\psi(-bx)}$, and $q^*i^*G$ is constant. Thus the geometric
sheaf underlying $H$ is a finite direct sum of linear characters, with
multiplicities. It is nonzero because $M\ne0$ and $j^*j_*M\simeq M$.
Projection onto a nonzero summand gives a quotient
$\mathcal L_{\psi(ax)}$ for some $a\in\bar k_0$. Restricting along
$j$ gives a quotient $\mathcal L_{\psi(ax)}|_U$ of the geometric
sheaf underlying $M$, hence a geometric irreducible constituent.
The nonexceptionality hypothesis excludes this constituent, proving
the final assertion.
