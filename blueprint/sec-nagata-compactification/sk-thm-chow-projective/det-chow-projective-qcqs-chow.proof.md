+++
kind  = "proof"
of    = "det-chow-projective-qcqs-chow"
uses = ["thm-chow-lemma", "prop-nagata-finite-type-closed-in-fp", "prop-nagata-noetherian-inverse-system", "lemma-nagata-separated-eventually", "def-nagata-projective-space-base-change"]
+++
*Step 1: envelope.* By [prop-nagata-finite-type-closed-in-fp] there is a
closed immersion $e:X\hookrightarrow X_0$ over $S$ with $f_0:X_0\to S$
separated and of finite presentation.

*Step 2: Noetherian model.* By [prop-nagata-noetherian-inverse-system],
$S=\varprojlim_\lambda S_\lambda$ for a cofiltered system of schemes of finite
type over $\mathbf Z$ (hence Noetherian) with affine transition maps. By
[lemma-nagata-separated-eventually] there are an index $\lambda$ and a
separated morphism of finite presentation $f_\lambda:X_\lambda\to S_\lambda$
with $X_0\cong X_\lambda\times_{S_\lambda}S$ over $S$. Since $S_\lambda$ is
Noetherian, $f_\lambda$ is separated of finite type over a Noetherian base.

*Step 3: Noetherian Chow.* By [thm-chow-lemma] applied to $f_\lambda$, there
are a finite set $N$, a proper surjective
$\pi_\lambda:\widetilde X_\lambda\to X_\lambda$ and an immersion
$i_\lambda:\widetilde X_\lambda\to\mathbf P^N_{S_\lambda}$ with
$q_{S_\lambda}i_\lambda=f_\lambda\pi_\lambda$.

*Step 4: base change to $S$.* Put
$\widetilde X_0=\widetilde X_\lambda\times_{S_\lambda}S$. The base change
$\pi_0:\widetilde X_0\to X_\lambda\times_{S_\lambda}S\cong X_0$ of
$\pi_\lambda$ is proper and surjective, these properties being stable under
base change. The base change $i_0:\widetilde X_0\to
\mathbf P^N_{S_\lambda}\times_{S_\lambda}S=\mathbf P^N_S$
([def-nagata-projective-space-base-change]) of $i_\lambda$ is an immersion,
and $q_Si_0=f_0\pi_0$.

*Step 5: restriction to $X$.* Put $\widetilde X=\widetilde X_0\times_{X_0}X$
with projections $\pi:\widetilde X\to X$ and $e':\widetilde X\to
\widetilde X_0$. Then $\pi$ is the base change of $\pi_0$ along $e$, hence
proper and surjective, and $e'$ is the base change of the closed immersion
$e$, hence a closed immersion. The composite $i_S=i_0\circ e'$ is a closed
immersion followed by an immersion, hence an immersion, and
$q_Si_S=q_Si_0e'=f_0\pi_0e'=f_0e\pi=f\pi$.
