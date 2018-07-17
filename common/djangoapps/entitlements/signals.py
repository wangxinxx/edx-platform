"""
Entitlements related signal handlers.
"""

from django.dispatch import receiver

from entitlements.models import CourseEntitlement
from student.signals import UNENROLL_DONE


@receiver(UNENROLL_DONE)
def unenroll_entitlement(sender, course_enrollment=None, skip_refund=False, **kwargs):  # pylint: disable=unused-argument
    """
    Un-enroll user from entitlement upon course run un-enrollment if exist.
    """
    CourseEntitlement.unenroll_entitlement(course_enrollment)
