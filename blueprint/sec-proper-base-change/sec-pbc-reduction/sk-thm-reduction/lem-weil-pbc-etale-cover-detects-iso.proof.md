+++
kind  = "proof"
of    = "lem-weil-pbc-etale-cover-detects-iso"
uses  = ["def-weil-pbc-inverse-image", "def-weil-geometric-point", "lemma-openclosed-stalk-upperstar", "def-weil-pbc-geometric-stalks", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
**Step 1.** *The easy direction.* If $\varphi$ is an isomorphism with inverse $\psi$, then $t_i^{-1}$, being a functor [def-weil-pbc-inverse-image], sends $\psi\circ\varphi=\mathrm{id}_G$ and $\varphi\circ\psi=\mathrm{id}_H$ to $t_i^{-1}\psi\circ t_i^{-1}\varphi=\mathrm{id}$ and $t_i^{-1}\varphi\circ t_i^{-1}\psi=\mathrm{id}$; so every $t_i^{-1}\varphi$ is an isomorphism.

**Step 2.** *Lifting a geometric point.* Assume every $t_i^{-1}\varphi$ is an isomorphism, and let $t\in T$. Since the family $(t_i)$ is jointly surjective there are $i\in I$ and $s\in T_i$ with $t_i(s)=t$. Let $\bar s:\operatorname{Spec}\Omega\to T_i$ be the geometric point at an algebraic closure $\Omega$ of $\kappa(s)$ [def-weil-geometric-point]; then $\bar t=t_i\circ\bar s$ is a geometric point of $T$ over $t$, with algebraically closed field $\Omega$. (If $I=\emptyset$ then $T=\emptyset$ and there is nothing to prove.)

**Step 3.** *The stalk of the pullback is the stalk at the image.* There is an isomorphism $c_K:(t_i^{-1}K)_{\bar s}\xrightarrow{\sim}K_{t_i\circ\bar s}=K_{\bar t}$ of stalks [def-weil-pbc-geometric-stalks], natural in the sheaf $K$ on $T_{\Et}$ [lemma-openclosed-stalk-upperstar] (Stacks 03Q1 (3)). Naturality applied to $\varphi:G\to H$ gives $\varphi_{\bar t}\circ c_G=c_H\circ(t_i^{-1}\varphi)_{\bar s}$. The stalk at $\bar s$ is a functor, so it sends the isomorphism $t_i^{-1}\varphi$ to an isomorphism; hence $\varphi_{\bar t}$ is an isomorphism.

**Step 4.** *Geometric stalks detect isomorphisms.* By steps 2 and 3, $\varphi$ is an isomorphism on the stalk at one geometric point over each point of $T$, with algebraically closed field. These stalks jointly detect isomorphisms [lemma-weil-pbc-geometric-stalk-conservative], so $\varphi$ is an isomorphism.

*Source: Stacks project, Tag 0EZR, end of (1), made explicit through Tags 03PU and 03Q1.*
