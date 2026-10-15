+++
kind = "proof"
of = "det-def-sfb-shriek-base-change-morphism-compactification"
+++
1. Since $p\circ(i\circ g')=f\circ g'=g\circ f'$, the pair $(i\circ g',f')$ defines a unique
   $i'\colon X'\to Z'=Z\times_YY'$ with $\bar g i'=ig'$ and $p'i'=f'$. The right square is cartesian by
   definition of $Z'$. Stacking the left square on top of the right one along their common edge
   $\bar g$ gives the outer square with top $g'$, left side $p'i'=f'$, right side $pi=f$ and bottom
   $g$, which is the given cartesian square. By the pasting law for pullbacks (if the lower square and
   the outer square are cartesian, so is the upper one), the left square is cartesian.
2. By 1, $i'$ is the base change of $i$ along $\bar g$. Open immersions and quasi-compact morphisms
   are stable under base change, so $i'$ is a quasi-compact open immersion. Likewise $p'$ is the base
   change of the proper morphism $p$ along $g$, and properness is stable under base change. Together
   with $f'=p'i'$, this says $c'$ is a compactification of $f'$.
3. The structure morphism of $Z'$ is the composite of $p'$ with the structure morphism of $Y'$; both
   are separated and of finite type (proper morphisms are separated and of finite type), hence so is
   the composite. The morphisms $p'$, $\bar g$ are $k$-morphisms as projections of a fibre product of
   $k$-schemes, and $i'$ is one because $p'i'=f'$ is.
