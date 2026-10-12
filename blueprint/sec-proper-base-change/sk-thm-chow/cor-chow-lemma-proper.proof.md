+++
kind  = "proof"
of    = "cor-chow-lemma-proper"
uses = ["def-nagata-affine-proj", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-proper-to-separated-target"]
+++
A proper morphism is separated and of finite type, so [thm-chow-lemma]
applies and yields $\pi\colon X'\to X$ and an immersion
$i\colon X'\to\mathbf P^n_S$ with the stated properties. Both $f$ and $\pi$
are proper, hence so is $f\circ\pi\colon X'\to S$. Since $\mathbf P^n_S\to S$
is separated, 01W6 shows that $i$ is universally closed; in
particular $i(X')\subseteq\mathbf P^n_S$ is closed, and an immersion with
closed image is a closed immersion by 01IQ. Thus $f\circ\pi$
is the composition of the closed immersion $i$ with the structure morphism
$\mathbf P^n_S\to S$, so $X'$ is projective over $S$.
