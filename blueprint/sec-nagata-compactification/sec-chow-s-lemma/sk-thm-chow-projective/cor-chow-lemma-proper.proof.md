+++
kind  = "proof"
of    = "cor-chow-lemma-proper"
uses = ["def-nagata-affine-proj", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-proper-to-separated-target"]
+++
A proper morphism is separated and of finite type, so [thm-chow-lemma]
applies and yields $\pi\colon X'\to X$ and an immersion
$i\colon X'\to\mathbf P^N_S$ with $p\circ i=f\circ\pi$, where
$p\colon\mathbf P^N_S\to S$. Both $f$ and $\pi$
are proper, hence so is $p\circ i=f\circ\pi\colon X'\to S$. Since $p$
is separated, 01W6 shows that $i$ is universally closed; in
particular $i(X')\subseteq\mathbf P^N_S$ is closed, and an immersion with
closed image is a closed immersion by 01IQ.
