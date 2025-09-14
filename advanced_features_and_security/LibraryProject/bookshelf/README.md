# Groups & Permissions Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Usage
Permissions are enforced in views using `@permission_required`.
Assign users to groups in Django admin to control access.
